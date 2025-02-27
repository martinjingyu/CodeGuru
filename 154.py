import subprocess
import re

def parse_and_execute(input_string):
    # Check if the string is likely an arithmetic expression
    is_arithmetic = re.match(r'^[\d\s\+\-\*\/\(\)]+$', input_string)

    try:
        if is_arithmetic:
            # Evaluate the arithmetic expression
            result = eval(input_string)
            return result
        else:
            # Execute the system command
            process = subprocess.Popen(input_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if process.returncode == 0:
                return output.decode().strip()
            else:
                return error.decode().strip()
    except Exception as e:
        return str(e)

# Example usage:
print(parse_and_execute("2 + 3"))  # Output: 5
print(parse_and_execute("dir"))    # Output: The contents of the directory (varies by platform)