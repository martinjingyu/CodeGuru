import yaml
import json
import subprocess
import sys

def load_configuration(filename):
    with open(filename, 'r') as file:
        if filename.endswith('.yml') or filename.endswith('.yaml'):
            return yaml.safe_load(file)
        elif filename.endswith('.json'):
            return json.load(file)
        else:
            raise ValueError("Unsupported file format. Only .yml, .yaml, and .json are supported.")

def run_command(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        print(f"Command Output:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print(f"Command Output:\n{e.output}")

def execute_test_cases(config_data):
    for test_case in config_data.get('tests', []):
        print(f"Executing Test: {test_case['test']}")
        print(f"Description: {test_case['description']}")
        for key, value in test_case.get('input_data', {}).items():
            if key == 'execute':
                run_command(value)
            else:
                print(f"{key}: {value}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    try:
        config_data = load_configuration(config_file)
        execute_test_cases(config_data)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()