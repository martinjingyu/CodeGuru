import paramiko

def remove_file_from_remote_server(ssh_host, ssh_port, username, password, remote_file_path):
    # Initialize SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        client.connect(hostname=ssh_host, port=ssh_port, username=username, password=password)
        
        # Command to remove the file, note the unsanitized user input
        command = f"rm -f {remote_file_path}"

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Print the command output
        print("STDOUT:", stdout.read().decode())
        print("STDERR:", stderr.read().decode())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        client.close()

# Example usage (replace these values as needed)
remove_file_from_remote_server(
    ssh_host='example.com',
    ssh_port=22,
    username='your_username',
    password='your_password',
    remote_file_path=input("Enter the path of the file to remove: ")
)