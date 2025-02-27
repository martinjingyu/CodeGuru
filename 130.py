def execute_dynamic_script(script):
    """
    Executes a provided Python script dynamically using exec() and returns the result and any error messages.

    Args:
    script (str): A string containing the Python code to be executed.

    Returns:
    tuple: A tuple containing the result of the execution and any error messages.
    """
    # Dictionaries to store local and global variables
    local_vars = {}
    global_vars = {}
    
    # Initialize variables to store execution results and errors
    execution_result = None
    error_message = None

    try:
        # Execute the script
        exec(script, global_vars, local_vars)
        
        # Assuming the script returns a value by assigning it to a variable named 'result'
        # This is a common pattern when using exec for dynamic execution
        execution_result = local_vars.get('result', None)
        
    except Exception as e:
        # Capture and log the error
        error_message = str(e)

    # Return the result and any error message
    return execution_result, error_message

# Example usage:
script = """
result = 2 + 2
"""

result, error = execute_dynamic_script(script)
print("Result:", result)  # Output: Result: 4
print("Error:", error)    # Output: Error: None