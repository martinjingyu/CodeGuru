import subprocess
import os

def send_email(sender, recipient, subject, body):
    """
    Sends an email using the sendmail command-line tool.

    Parameters:
    sender (str): The sender's email address.
    recipient (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body content of the email.
    """
    try:
        # Create the email headers and body
        email_message = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"

        # Execute the sendmail command
        process = subprocess.Popen(
            ['sendmail', recipient],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={"MAILTO": recipient}  # Ensure sendmail knows the recipient
        )
        
        # Send the email message and capture output
        stdout_data, stderr_data = process.communicate(input=email_message.encode())

        # Check for errors
        if process.returncode != 0:
            print(f"Error sending email:\n{stderr_data.decode()}")
        else:
            print("Email sent successfully.")

    except FileNotFoundError:
        print("Error: 'sendmail' command not found. Please ensure sendmail is installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# send_email('sender@example.com', 'recipient@example.com', 'Test Subject', 'This is a test email body.')