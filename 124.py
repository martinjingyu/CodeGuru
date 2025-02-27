import subprocess

def execute_commands(commands):
    """
    Executes a list of command strings and returns a list of CompletedProcess objects.

    :param commands: List of command strings to be executed.
    :return: List of CompletedProcess objects representing the results of the commands.
    """
    def run_command(command):
        try:
            # Execute the command
            result = subprocess.run(
                command, 
                shell=True, 
                check=False, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )
            return result
        except Exception as e:
            # Return an error message in case of an exception
            result = subprocess.CompletedProcess(
                args=command,
                returncode=1,
                stdout='',
                stderr=str(e)
            )
            return result

    # Use map to apply run_command to each command in the list
    results = list(map(run_command, commands))
    return results

# Example usage:
# commands = ["echo Hello", "ls non_existent_dir", "echo World"]
# results = execute_commands(commands)
# for result in results:
#     print(f"Command: {result.args}")
#     print(f"Return Code: {result.returncode}")
#     print(f"Output: {result.stdout}")
#     print(f"Error: {result.stderr}")