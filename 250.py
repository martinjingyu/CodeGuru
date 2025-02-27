import subprocess

def execute_commands(commands):
    """
    Executes a list of shell commands and returns their outputs.

    :param commands: A list of command strings to be executed.
    :return: A list of outputs from each command.
    """
    def run_command(command):
        # Execute the command and capture the output
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        # Return the standard output
        return result.stdout.strip()

    # Use map to apply run_command to each command in the list
    outputs = list(map(run_command, commands))
    return outputs

# Example usage:
commands = ['echo "Hello, World!"', 'ls', 'uname -a']
outputs = execute_commands(commands)
for output in outputs:
    print(output)