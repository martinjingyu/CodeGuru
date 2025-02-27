import subprocess

def create_group_membership(username, group_names):
    """
    Adds a user to specified groups using the usermod command.

    Args:
    username (str): The username of the user to modify.
    group_names (list): A list of group names to add the user to.
    """
    # Join the group names into a space-separated string
    groups = ' '.join(group_names)
    
    # Construct the usermod command
    command = f"usermod -aG {groups} {username}"
    
    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print(f"User '{username}' added to groups: {', '.join(group_names)}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage:
# create_group_membership('john_doe', ['group1', 'group2'])