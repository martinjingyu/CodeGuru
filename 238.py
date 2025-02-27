def execute_script_with_files(file_contents, script):
    """
    Executes a Python script with dynamically loaded files as globals.

    :param file_contents: A dictionary mapping file paths (strings) to file contents (strings).
    :param script: A string containing the Python script to execute.
    :return: The output of the executed script (assuming it prints something or modifies a variable).
    """
    # Create a dictionary to serve as the global namespace for the script execution
    global_namespace = {}
    
    # Populate the global namespace with file contents using the file paths as variable names
    for file_path, content in file_contents.items():
        global_namespace[file_path] = content
    
    # Prepare to capture print outputs if any (simulating a way to "return" the print statements)
    import io
    import sys
    
    # Create a string buffer to capture the output
    captured_output = io.StringIO()
    # Backup the original stdout
    original_stdout = sys.stdout
    # Redirect stdout to the buffer
    sys.stdout = captured_output

    try:
        # Use exec to execute the script with the global namespace we prepared
        exec(script, global_namespace)
    except Exception as e:
        # Ensure that stdout is restored even if an error occurs
        sys.stdout = original_stdout
        raise e  # Re-raise the exception after handling
        
    # Restore stdout
    sys.stdout = original_stdout
    
    # Return the captured output
    return captured_output.getvalue()

# Example usage:
file_contents_dict = {
    'file1.txt': 'This is the content of file 1.\n',
    'file2.txt': 'This is the content of file 2.\n'
}

script_to_execute = """
print("Executing script with files loaded as globals...")

file1_content = file1.txt.split('\\n')
file2_content = file2.txt.split('\\n')

print("File 1 content:")
print(file1_content)
print("File 2 content:")
print(file2_content)
"""

result = execute_script_with_files(file_contents_dict, script_to_execute)
print("Execution result:")
print(result)