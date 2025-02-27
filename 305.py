import subprocess

def execute_commands(commands):
    """
    Execute a list of shell commands and return their outputs.

    Parameters:
    commands (list): A list of command strings to be executed.

    Returns:
    list: A list containing the outputs of the executed commands.
    """
    # Define a function to execute a single command and capture its output
    def run_command(command):
        try:
            # Run the command and capture the output
            result = subprocess.run(
                command, shell=True, check=True, text=True, capture_output=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            # In case of an error, return the error output
            return e.stderr.strip()
        except Exception as e:
            # Handle any other exceptions that may occur
            return str(e)

    # Use map to apply run_command to each command in the list
    outputs = map(run_command, commands)

    # Convert the map object to a list and return it
    return list(outputs)

# Example usage:
commands = ["echo Hello, World!", "ls -l", "invalid_command"]
outputs = execute_commands(commands)
for output in outputs:
    print(output)