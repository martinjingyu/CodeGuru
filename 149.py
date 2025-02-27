import subprocess

def configure_network_interface(interface_name, ip_address):
    """
    Configure a network interface with the given IP address.

    :param interface_name: Name of the network interface (e.g., 'eth0').
    :param ip_address: IP address to assign to the interface (e.g., '192.168.1.10').
    """
    try:
        # Construct the ifconfig command to assign the IP address to the interface
        command = ["sudo", "ifconfig", interface_name, ip_address, "up"]
        
        # Execute the command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Output the result
        print("Command executed successfully:")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print("An error occurred while configuring the network interface:")
        print(e.stderr)

# Example usage:
# configure_network_interface("eth0", "192.168.1.10")