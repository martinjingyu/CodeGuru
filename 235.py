def analyze_script_for_errors(file_path):
    try:
        with open(file_path, 'r') as file:
            script_content = file.read()
    except IOError as e:
        return [f"File error: {e}"]

    try:
        compiled_script = compile(script_content, file_path, 'exec')
    except SyntaxError as e:
        # Extract the line number and error message
        error_details = [(e.lineno, e.msg)]
        return error_details
    
    try:
        exec(compiled_script)
    except Exception as e:
        return [f"Runtime error: {e}"]
    
    return "Script executed successfully."

# Usage example:
# result = analyze_script_for_errors('path_to_your_script.py')
# print(result)