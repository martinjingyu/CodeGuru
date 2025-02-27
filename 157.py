import subprocess

def execute_command():
    # Get user input
    command = input("Enter the command to execute: ")
    
    # Use subprocess.Popen without validation or sanitization
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Capture the output and errors
    stdout, stderr = process.communicate()

    # Display the output and errors
    print("Output:")
    print(stdout.decode())
    print("Errors:")
    print(stderr.decode())

# Example call to the function
if __name__ == "__main__":
    execute_command()