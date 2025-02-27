import csv
import subprocess

def load_csv(file_path):
    """Load data from a CSV file."""
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

def execute_command(command, input_data):
    """Execute a command using subprocess."""
    try:
        # Run the command with input data
        result = subprocess.run(command, input=input_data, text=True, capture_output=True, shell=True)
        # Print the result
        print(f"Output:\n{result.stdout}")
        print(f"Error:\n{result.stderr}")
    except Exception as e:
        print(f"An error occurred while executing the command: {e}")

def main():
    csv_file_path = input("Enter the path to the CSV file: ")
    data = load_csv(csv_file_path)
    
    if not data:
        print("No data to process.")
        return

    for entry in data:
        command = entry.get("Command", "")
        description = entry.get("Description", "")
        input_data = entry.get("InputData", "").strip()

        print("\nExecuting the following command:")
        print(f"Description: {description}")
        print(f"Command: {command}")
        print(f"Input Data: {input_data}")

        user_decision = input("Do you want to execute this command? (yes/no): ").strip().lower()
        
        if user_decision == 'yes':
            execute_command(command, input_data)
        elif user_decision == 'no':
            print("Skipping command.")
        else:
            print("Invalid input. Skipping command.")

if __name__ == "__main__":
    main()