import yaml
import json
import subprocess
import os
import argparse

def parse_config(config_file):
    with open(config_file, 'r') as file:
        if config_file.endswith('.yaml') or config_file.endswith('.yml'):
            config = yaml.safe_load(file)
        elif config_file.endswith('.json'):
            config = json.load(file)
        else:
            raise ValueError("Unsupported file format. Please use JSON or YAML.")
    return config

def print_tests(tests):
    for test in tests:
        print(f"Name: {test['name']}")
        print(f"Description: {test['description']}")
        print(f"Parameters:")
        for param, desc in test['params'].items():
            print(f"  {param}: {desc}")
        print()

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' failed with return code {e.returncode}")
        print(e.output.decode())

def main():
    parser = argparse.ArgumentParser(description="Run tests based on a config file.")
    parser.add_argument("config", help="Configuration file in YAML or JSON format")
    args = parser.parse_args()

    config = parse_config(args.config)
    tests = config['tests']

    print("Available tests:")
    print_tests(tests)

    test_name = input("Enter the name of the test you want to run: ")
    selected_test = next((test for test in tests if test['name'] == test_name), None)

    if selected_test:
        print("Selected test:")
        print(f"Name: {selected_test['name']}")
        print(f"Description: {selected_test['description']}")
        command = input("Enter the command to execute: ")
        if command in selected_test['params']:
            print("Running command...")
            run_command(command)
        else:
            print("Command not found in test parameters.")
    else:
        print("Test not found.")

if __name__ == "__main__":
    main()