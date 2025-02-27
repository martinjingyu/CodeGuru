import subprocess
import logging
import sqlite3
import smtplib
from email.message import EmailMessage


def execute_command(command):
    # Configure logging
    logging.basicConfig(filename='command_output.log', level=logging.INFO)

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    exit_code = process.returncode

    # Convert bytes to string
    output = stdout.decode('utf-8') if stdout else ''
    error = stderr.decode('utf-8') if stderr else ''
    
    # Log the command and its output
    logging.info(f'Command: {command}')
    logging.info(f'Output: {output}')
    if exit_code != 0:
        logging.error(f'Error: {error}')

    # Determine if the command was successful
    status = 'success' if exit_code == 0 else 'failure'

    # Save command history to the database
    save_command_history(command, status, error if exit_code != 0 else output)

    # Notify via email if the command failed
    if exit_code != 0:
        send_email_notification(command, error)

    return exit_code, output


def save_command_history(command, status, output):
    connection = sqlite3.connect('command_history.db')
    cursor = connection.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS command_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT,
            status TEXT,
            output TEXT
        )
    ''')

    # Insert the command history
    cursor.execute('''
        INSERT INTO command_history (command, status, output) VALUES (?, ?, ?)
    ''', (command, status, output))

    connection.commit()
    connection.close()


def send_email_notification(command, error):
    email_sender = 'your_email@example.com'
    email_receiver = 'receiver_email@example.com'
    email_password = 'your_email_password'
    subject = 'Command Execution Failed'
    
    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    body = f'The command "{command}" failed with error:\n\n{error}'
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
            server.login(email_sender, email_password)
            server.send_message(msg)
        print('Email notification sent successfully.')
    except Exception as e:
        print(f'Failed to send email: {e}')


# Example usage:
if __name__ == "__main__":
    command = 'ls -la'  # Change this to any command you want to test
    execute_command(command)