def execute_config_file(file_path):
    """
    Parses a configuration file and executes each command found within.
    
    Parameters:
    - file_path: str, path to the configuration file to be executed.
    
    Raises:
    - FileNotFoundError: If the file does not exist.
    - Exception: Any exception raised during the execution of the commands.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip whitespace and ignore comments or empty lines
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Execute the command line
                try:
                    exec(line)
                except Exception as e:
                    print(f"Error executing line '{line}': {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage
# execute_config_file('path_to_config_file.txt')