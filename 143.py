import subprocess

def execute_user_command():
    user_input = input("Enter the command you want to execute: ")
    
    # Using shell=True to allow the command to be executed as a shell command
    try:
        process = subprocess.Popen(user_input, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Getting output and error streams
        output, error = process.communicate()

        # Decoding the output and error from bytes to string
        if output:
            print("Output:")
            print(output.decode())
        if error:
            print("Error:")
            print(error.decode())

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    execute_user_command()