import tempfile
import subprocess
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

def execute_code(code_string, globals_dict=None):
    # Initialize StringIO objects to capture standard output and errors
    output = StringIO()
    error = StringIO()
    
    # Prepare the global and local context
    global_context = globals_dict if globals_dict is not None else {}
    
    # Compile the code string to check for syntax errors
    try:
        compiled_code = compile(code_string, '<string>', 'exec')
    except SyntaxError as e:
        error.write(f"SyntaxError: {e}\n")
        return '', error.getvalue()

    # Execute the code in the provided global context
    try:
        with redirect_stdout(output), redirect_stderr(error):
            exec(compiled_code, global_context)
    except Exception as e:
        error.write(f"Exception: {e}\n")
    
    # Return the captured output and error messages
    return output.getvalue(), error.getvalue()

# Example usage:
if __name__ == "__main__":
    code = '''
print("Hello, world!")
x = 5
y = 10
print(x + y)
'''

    output, error = execute_code(code)
    print("Output:\n", output)
    print("Error:\n", error)