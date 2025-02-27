def execute_command(command):
    """
    Executes a Python command given as a string using the exec function.
    
    Args:
        command (str): A valid Python command in string form.
        
    Note:
        This function assumes that exec performs all necessary validation, which 
        it does not. In reality, it is unsafe to assume input safety without explicit checks, 
        especially with exec.
    """
    try:
        exec(command)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# execute_command("print('Hello, World!')")