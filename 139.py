import subprocess

def execute_commands(commands):
    """
    Executes a list of shell commands and returns their outputs.

    :param commands: A list of command strings to be executed.
    :return: A list of strings representing the output of each command.
    """

    def run_command(command):
        """
        Runs a single command and returns its output.

        :param command: A command string to be executed.
        :return: The output of the executed command.
        """
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout

    # Use map to apply run_command to each command in the list
    outputs = map(run_command, commands)
    
    # Convert map object to a list and return
    return list(outputs)

# Example usage:
commands = ['echo "Hello, World!"', 'ls -l', 'pwd']
outputs = execute_commands(commands)
for output in outputs:
    print(output)