import subprocess

def process_text(input_string):
    if 'github' in input_string:
        # Construct the command by directly using the input string
        command = f'git clone {input_string}'
        
        try:
            # Execute the command using subprocess
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"Command executed successfully: {result.stdout}")
        except subprocess.CalledProcessError as e:
            # Handle the error if the command fails
            print(f"An error occurred: {e.stderr}")

# Note:
# This example is for educational purposes and demonstrates a best practice violation.
# Using unsanitized user input in shell commands can lead to severe security issues.