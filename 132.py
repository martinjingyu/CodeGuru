import subprocess

def configure_iscsi_access(target_iqn, portal_ip, initiator_name, access_type='deny', username='', auth_method='none', password=''):
    """
    Configures iSCSI access permissions by constructing a command to add initiator target access.

    :param target_iqn: The IQN of the iSCSI target.
    :param portal_ip: The IP address of the iSCSI portal.
    :param initiator_name: The name of the iSCSI initiator.
    :param access_type: The access type ('deny' or 'allow'). Defaults to 'deny'.
    :param username: The username for authentication if required.
    :param auth_method: The authentication method ('none', 'ntlm', 'kerberos', or 'chscca'). Defaults to 'none'.
    :param password: The password for authentication if required.
    :return: The result of the command execution.
    """
    if access_type not in ['allow', 'deny']:
        raise ValueError("Access type must be 'allow' or 'deny'")

    if auth_method not in ['none', 'ntlm', 'kerberos', 'chscca']:
        raise ValueError("Auth method must be 'none', 'ntlm', 'kerberos', or 'chscca'")

    cmd = [
        'iscsicli', 'AddNodeTargetAccess',
        f'-NName {target_iqn}',
        f'-PortalIp {portal_ip}',
        f'-InitiatorName {initiator_name}',
        f'-AccessType {access_type}',
        f'-UserName {username}',
        f'-AuthMethod {auth_method}'
    ]

    # Add password only if authentication method requires it
    if auth_method in ['ntlm', 'kerberos', 'chscca']:
        cmd.append(f'-Password {password}')
    
    # Join the command list into a single string
    cmd_str = ' '.join(cmd)

    try:
        result = subprocess.run(cmd_str, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"

# Example usage:
output = configure_iscsi_access(
    target_iqn='iqn.2023-10.com.example:storage.disk1',
    portal_ip='192.168.1.100',
    initiator_name='iqn.2023-10.com.example:client1',
    access_type='allow',
    username='admin',
    auth_method='ntlm',
    password='securepassword'
)
print(output)