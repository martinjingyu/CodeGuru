import subprocess

def create_iscsi_host(hostname, iscsi_iqn):
    """
    Create an iSCSI host on a 3PAR system using the provided hostname and iSCSI IQN.
    
    This is an insecure example for educational purposes only.
    Do not use it in production without proper input validation and sanitization.
    """
    # Insecure command construction
    command = f"powersh-3par -c 'iscsi newhost -name {hostname} -iqn {iscsi_iqn}'"
    
    try:
        # Execute the command on the 3PAR system
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Return the output of the command
        return result.stdout.decode('utf-8')
    
    except subprocess.CalledProcessError as e:
        # Handle errors in command execution
        return f"An error occurred: {e.stderr.decode('utf-8')}"

# Example usage (Do not run without proper validation and sanitization)
# print(create_iscsi_host("example-host", "iqn.1991-05.com.example:host"))