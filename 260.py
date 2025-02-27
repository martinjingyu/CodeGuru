import csv
import subprocess

def execute_commands_from_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            command = row['command']
            description = row['description']
            input_value = row.get('input_value', None)

            # Display the command and description
            print(f"Executing: {command} ({description})")

            # Handle optional input value
            if input_value:
                response = input(f"Enter {input_value} (press Enter to skip): ")
                if response:
                    command = command.format(input_value=response)

            try:
                # Execute the command
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = process.communicate()

                # Display output or error
                if error:
                    print(f"Error: {error.decode('utf-8')}")
                else:
                    print(f"Output: {output.decode('utf-8')}")
            except Exception as e:
                print(f"Failed to execute command: {command} - {e}")

            # Ask if the user wants to skip the next command
            choice = input("Skip next command? (y/n): ")
            if choice.lower() == 'y':
                continue
            elif choice.lower() == 'n':
                break
            else:
                print("Invalid choice, continuing to next command.")

# Prompt user for CSV file path
csv_file_path = input("Enter the path to the CSV file: ")

# Call the function with the provided CSV file path
execute_commands_from_csv(csv_file_path)