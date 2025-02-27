import subprocess
import re

def validate_and_execute(inputs):
    """
    Validates and executes actions based on user inputs.
    
    :param inputs: A list of strings, each representing a user input.
    """
    # Define validation criteria and corresponding actions
    validation_actions = {
        'greet': lambda name: f"Hello, {name}!",
        'run': lambda command: subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    }
    
    # Regular expression to extract command after 'run'
    run_command_regex = r'^run\s+(.*)$'
    
    for input_str in inputs:
        try:
            # Check if input is for running a command
            if input_str.startswith('run'):
                match = re.match(run_command_regex, input_str)
                if match:
                    command = match.group(1).strip()
                    if command:
                        # Execute the system command
                        print(f"Executing command: {command}")
                        result = validation_actions['run'](command)
                        print(f"Command output: {result.stdout.decode().strip()}")
                        if result.stderr:
                            print(f"Command error: {result.stderr.decode().strip()}", file=sys.stderr)
                    else:
                        raise ValueError("No command specified after 'run'.")
                else:
                    raise ValueError("Invalid command format. Use 'run <command>'.")
            
            else:
                # Split input into action and potential arguments
                parts = input_str.split(maxsplit=1)
                action = parts[0]
                argument = parts[1] if len(parts) > 1 else None
                
                # Validate and execute action
                if action in validation_actions:
                    if action == 'greet' and argument:
                        response = validation_actions[action](argument)
                        print(response)
                    else:
                        raise ValueError(f"Action '{action}' requires an argument.")
                else:
                    raise ValueError(f"Unknown action '{action}'.")
        
        except Exception as e:
            print(f"Error processing input '{input_str}': {e}", file=sys.stderr)

# Example usage
user_inputs = [
    "greet Alice",
    "run echo Hello, World!",
    "run ls -l",
    "greet",
    "run"
]

validate_and_execute(user_inputs)