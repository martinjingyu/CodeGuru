import csv
import subprocess

def read_commands(filename):
    """Read commands from a CSV file."""
    commands = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            commands.append({
                'command': row['command'].strip(),
                'description': row['description'].strip(),
                'input': row['input'].strip()
            })
    return commands

def execute_command(command, input_value=None):
    """Execute a shell command with optional input."""
    try:
        # Use subprocess to execute the command
        process = subprocess.Popen(
            command, 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            shell=True,
            text=True
        )
        
        # Send input to the command if provided
        stdout, stderr = process.communicate(input=input_value)
        return stdout, stderr
    except Exception as e:
        return "", str(e)

def main():
    commands = read_commands('commands.csv')

    for cmd in commands:
        command = cmd['command']
        description = cmd['description']
        input_value = cmd['input']

        while True:
            print(f"\nCommand: {command}")
            print(f"Description: {description}")
            print("1: Run Command")
            print("2: Skip Command")
            print("3: Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                stdout, stderr = execute_command(command, input_value)
                print("\nOutput:")
                print(stdout)
                if stderr:
                    print("Error:")
                    print(stderr)
                break
            elif choice == '2':
                print("Skipping command.")
                break
            elif choice == '3':
                print("Exiting script.")
                return
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()