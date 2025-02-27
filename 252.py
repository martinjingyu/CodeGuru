import paramiko

def execute_ssh_command(host, port, username, password, command):
    # Initialize the SSH client
    client = paramiko.SSHClient()
    
    # Automatically add the host key (without verification)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the SSH server
        client.connect(host, port=port, username=username, password=password)
        
        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)
        
        # Read the output and errors
        output = stdout.read().decode()
        error = stderr.read().decode()
        
        # Print the output and errors
        print("Output:")
        print(output)
        if error:
            print("Error:")
            print(error)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the client connection
        client.close()

# Example usage (replace with your actual credentials and command)
# execute_ssh_command('192.168.1.100', 22, 'user', 'password', 'ls -la')