import os
import socket
import paramiko

def create_directories_from_template(template_path, replacement_values):
    """
    Create directories from a template file by replacing placeholders.
    
    :param template_path: Path to the template file.
    :param replacement_values: Dictionary of placeholder replacements.
    """
    with open(template_path, 'r') as template_file:
        for line in template_file:
            # Replace placeholders with actual values
            for placeholder, value in replacement_values.items():
                line = line.replace('{{' + placeholder + '}}', value)
            
            # Create directories
            directory_path = line.strip()
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
                print(f"Directory created: {directory_path}")
            else:
                print(f"Directory already exists: {directory_path}")
            yield directory_path

def connect_to_server_and_send_dirs(hostname, port, username, password, directories):
    """
    Connect to a remote server and send the names of directories.
    
    :param hostname: The hostname of the server.
    :param port: Port number for SSH connection.
    :param username: Username for SSH login.
    :param password: Password for SSH login.
    :param directories: List of directory names to send.
    """
    try:
        # Create an SSH client and connect to the server
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=hostname, port=port, username=username, password=password)
        
        # Open a channel and execute a command to list the directory names
        command = 'echo ' + ' '.join(directories)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Print the command output
        print("Command output:", stdout.read().decode())
        print("Command errors:", stderr.read().decode())
        
    except Exception as e:
        print(f"Failed to connect or execute command: {e}")
    finally:
        ssh_client.close()

if __name__ == "__main__":
    # Define template path and replacement values
    template_path = 'path/to/template.txt'
    replacement_values = {
        'year': '2023',
        'month': '09',
        'day': '15'
    }
    
    # Define server connection details
    hostname = 'example.com'
    port = 22
    username = 'your_username'
    password = 'your_password'
    
    # Create directories from the template
    directory_paths = list(create_directories_from_template(template_path, replacement_values))
    
    # Extract directory names
    directory_names = [os.path.basename(dir_path) for dir_path in directory_paths]
    
    # Connect to the server and send directory names
    connect_to_server_and_send_dirs(hostname, port, username, password, directory_names)