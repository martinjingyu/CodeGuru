import subprocess

def ssh_connect(host, username, password, command):
    try:
        # Construct the SSH command
        ssh_command = [
            'sshpass', '-p', password,
            'ssh', f'{username}@{host}',
            command
        ]

        # Execute the command using subprocess
        result = subprocess.run(ssh_command, capture_output=True, text=True, check=True)

        # Print the output if the command was successful
        print("Command output:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to execute the SSH command:")
        print(e.stderr)
    except FileNotFoundError:
        print("Please ensure that 'sshpass' is installed and available in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
host = 'your.remote.server'
username = 'your_username'
password = 'your_password'
command = 'ls -l'  # Example command to run on the remote server

ssh_connect(host, username, password, command)