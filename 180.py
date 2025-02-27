import subprocess
import platform

def execute_remote_command(command):
    """
    Executes a remote command and returns the output.

    Args:
    - command (str): The command to be executed as a string.

    Returns:
    - str: The output of the command.
    """
    # Determine if the operating system is Windows
    is_windows = platform.system().lower() == 'windows'
    
    # Set the creationflags if the operating system is Windows to suppress the console window
    creationflags = 0x08000000 if is_windows else 0
    
    # Execute the command
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        creationflags=creationflags
    )

    # Return the standard output of the command
    return result.stdout if result.returncode == 0 else result.stderr

# Example usage:
# output = execute_remote_command("echo Hello, World!")
# print(output)