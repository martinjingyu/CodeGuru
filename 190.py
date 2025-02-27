import subprocess

def configure_iscsi(target_alias, target_ip, initiator_name):
    """
    Configure network settings for a storage device using iSCSI with user input directly used in the command.
    
    Parameters:
    - target_alias: The alias for the target iSCSI device.
    - target_ip: The IP address of the target iSCSI device.
    - initiator_name: The name of the iSCSI initiator.

    Note: This function uses user input directly in shell commands without validation or sanitization.
    """
    try:
        # Construct the iSCSI configuration command using user inputs directly
        command = f"iscsiadm -m node -T {target_ip} -p {target_ip} --login -n startup"
        
        # Print the command for demonstration (DO NOT log sensitive commands in production code)
        print(f"Executing command: {command}")
        
        # Execute the command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print the output of the command
        print("Output:", result.stdout)
        print("Error (if any):", result.stderr)
        
    except subprocess.CalledProcessError as e:
        # Handle errors in the subprocess
        print("An error occurred while executing the command:")
        print(e.stderr)

# Example usage (Do not use in production without proper sanitization and validation)
configure_iscsi("myTargetAlias", "192.168.1.100", "myInitiatorName")