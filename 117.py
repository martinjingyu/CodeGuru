import sys
import tempfile
import os
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

def execute_custom_code(code, globals_dict=None):
    if globals_dict is None:
        globals_dict = {}

    # Create a temporary file to store the code
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.py') as temp_file:
        temp_file_name = temp_file.name
        temp_file.write(code)
    
    # Prepare to capture output
    captured_output = StringIO()
    captured_errors = StringIO()

    try:
        # Redirect stdout and stderr
        with redirect_stdout(captured_output), redirect_stderr(captured_errors):
            # Execute the code
            with open(temp_file_name, 'r') as file:
                exec(file.read(), globals_dict)
    except Exception as e:
        captured_errors.write(f"Exception: {str(e)}\n")
    finally:
        # Clean up: remove temporary file
        try:
            os.remove(temp_file_name)
        except OSError as e:
            captured_errors.write(f"Error removing temporary file: {str(e)}\n")

    # Get the output and errors
    output = captured_output.getvalue()
    errors = captured_errors.getvalue()

    return output, errors

# Example usage:
code = """
print("Hello, World!")
x = 10
print(x)
print(unknown_variable)  # This will cause an error
"""

output, errors = execute_custom_code(code)
print("Output:\n", output)
print("Errors:\n", errors)