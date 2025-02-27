import os
import subprocess

def main():
    # Greet the user
    print("Python Script to Handle File Paths and Execute Commands")

    # Get user input for file paths and command
    input_file_path = input("Enter the path to the input file: ")
    output_file_path = input("Enter the path to the output file: ")
    command_to_execute = input("Enter the command to execute (use placeholders for file paths): ")

    # Insert file paths into the command string
    command = command_to_execute.format(input_file=input_file_path, output_file=output_file_path)

    # Print the command to be executed
    print(f"Executing command: {command}")

    # Execute the command
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Command executed successfully with output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error:\n{e.stderr}")

if __name__ == "__main__":
    main()