import csv
import subprocess
import sys

def execute_commands(csv_file):
    def execute_command(command, input_value=None):
        try:
            if input_value is not None:
                # Use subprocess with input and text to handle string input
                result = subprocess.run(
                    command, 
                    input=input_value,
                    text=True,
                    capture_output=True,
                    shell=True
                )
            else:
                # Execute the command without input
                result = subprocess.run(
                    command, 
                    capture_output=True,
                    shell=True
                )
            return result
        except Exception as e:
            print(f"Error executing command: {e}")
            return None

    def print_menu():
        print("\nMenu:")
        print("1. Execute next command")
        print("2. Skip current command")
        print("3. Exit")

    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for entry in csv_reader:
                command = entry['command']
                input_value = entry.get('input')
                description = entry['description']

                while True:
                    print_menu()
                    choice = input("Select an option: ")

                    if choice == '1':
                        # Execute the command
                        result = execute_command(command, input_value)
                        if result:
                            print(f"\nDescription: {description}\n")
                            print(f"Output:\n{result.stdout}")
                            if result.stderr:
                                print(f"Error:\n{result.stderr}")
                        break
                    elif choice == '2':
                        # Skip the command
                        print("Skipping...")
                        break
                    elif choice == '3':
                        # Exit the script
                        print("Exiting script.")
                        sys.exit(0)
                    else:
                        print("Invalid choice. Please try again.")

    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    except KeyError as e:
        print(f"CSV file is missing a necessary column: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# ensure your CSV file has columns named 'command', 'input' (optional), and 'description'
# execute_commands('commands.csv')