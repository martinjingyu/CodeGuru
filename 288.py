def execute_code_input(code_string):
    """
    Executes a string of Python code.

    Parameters:
    code_string (str): A string containing Python code to be executed.

    Returns:
    None
    """
    # Execute the code string using exec()
    try:
        exec(code_string)
    except Exception as e:
        print(f"An error occurred while executing the code: {e}")

# Example usage:
# execute_code_input("print('Hello, World!')")