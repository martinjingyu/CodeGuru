def run_complex_script(script: str):
    """
    Executes a Python script contained within a string using the exec() function.
    
    Parameters:
    script (str): A string containing the Python code to be executed.
    
    Returns:
    dict: A dictionary with two keys:
          - 'output': A list of strings capturing the printed output from the script.
          - 'error': The error message string if an exception occurs, else None.
    
    The function captures standard print output using a custom print function to
    redirect the output to a list that can be accessed after execution.
    
    For security reasons, ensure that the input script is from a trusted source
    or is constructed securely to prevent code injection.

    Example usage:
    --------------
    >>> script = '''
    ... def greet(name):
    ...     print(f"Hello, {name}!")
    ... greet("World")
    ... '''
    >>> result = run_complex_script(script)
    >>> result['output']
    ['Hello, World!']
    
    >>> script_untrusted = 'os.system("rm -rf /")' # Dangerous: DO NOT RUN!
    >>> run_complex_script(script_untrusted) # This should only be tested in a safe environment
    
    Security Note:
    ---------------
    Using `exec()` with untrusted code can lead to serious security vulnerabilities, including arbitrary code execution.
    It is highly recommended to either avoid using `exec()` or to sanitize and validate any input that will be executed as code.

    """
    # Initialize a dictionary to collect output and errors
    result = {'output': [], 'error': None}

    # Define a helper function to capture print output
    def custom_print(*args, **kwargs):
        """Custom print to capture output as strings in the list."""
        result['output'].append(' '.join(str(arg) for arg in args))

    # Define a local namespace for the script execution
    local_namespace = {
        '__builtins__': __builtins__,
        'print': custom_print  # Override print to capture output
    }

    try:
        # Execute the script in the local namespace
        exec(script, {"__builtins__": __builtins__}, local_namespace)
    except Exception as e:
        # Capture any exception that occurs during execution
        result['error'] = str(e)

    return result