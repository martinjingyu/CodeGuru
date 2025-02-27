import csv
import subprocess
import sys

def read_commands_from_csv(file_path):
    """Read and return a list of command entries from a CSV file."""
    commands = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                commands.append((row['Command'], row['Description'], row['Parameters']))
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)
    except KeyError as e:
        print(f"Missing expected column in CSV: {e}")
        sys.exit(1)
    return commands

def execute_command(command, parameters, description):
    """Execute the given command with optional parameters."""
    try:
        print(f"Executing command: {command}")
        if parameters:
            print(f"Description: {description}")
            print(f"With parameters: {parameters}")
            subprocess.run([command] + parameters.split(), check=True)
        else:
            print(f"Description: {description}")
            subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.\n")
    except subprocess.CalledProcessError:
        print(f"An error occurred while executing the command: {command}\n")

def main():
    csv_file_path = 'commands.csv'
    commands = read_commands_from_csv(csv_file_path)
    
    if not commands:
        print("No commands found in the CSV file.")
        sys.exit(0)
    
    for command, description, parameters in commands:
        print("Do you want to execute the following command? (yes/skip/terminate)")
        print(f"Command: {command}")
        print(f"Description: {description}")
        if parameters:
            print(f"With parameters: {parameters}")
        user_input = input("Enter your choice: ").strip().lower()
        
        if user_input == 'yes':
            execute_command(command, parameters, description)
        elif user_input == 'skip':
            print("Skipping command.\n")
        elif user_input == 'terminate':
            print("Terminating command execution process.\n")
            break
        else:
            print("Invalid input. Skipping command.\n")

if __name__ == "__main__":
    main()