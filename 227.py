import requests
import sys
import importlib.util
import traceback
import argparse

def retrieve_source_code(server_url, username, password):
    """
    This function retrieves the source code from a given server URL using basic authentication.

    Parameters:
    server_url (str): The URL of the server to retrieve the source code from.
    username (str): The username for authentication.
    password (str): The password for authentication.

    Returns:
    str: The source code retrieved from the server.
    """
    try:
        response = requests.get(server_url, auth=(username, password))
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving source code: {e}")
        sys.exit(1)

def execute_code(source_code, *args, **kwargs):
    """
    This function executes the retrieved source code with given arguments.

    Parameters:
    source_code (str): The source code to be executed.
    *args: Positional arguments to pass to the main function.
    **kwargs: Keyword arguments to pass to the main function.

    Returns:
    None
    """
    try:
        # Create a module spec and module from the source code
        module_name = "remote_module"
        spec = importlib.util.spec_from_loader(module_name, loader=None)
        module = importlib.util.module_from_spec(spec)

        # Execute the source code in the module's namespace
        exec(source_code, module.__dict__)

        # Find the main function and execute it
        if hasattr(module, 'main'):
            module.main(*args, **kwargs)
        else:
            print("No 'main' function found in the retrieved source code.")
    except Exception as e:
        print(f"Error executing code: {e}")
        traceback.print_exc()
        sys.exit(1)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Retrieve and execute source code from a server.")
    parser.add_argument('server_url', type=str, help='URL of the server to retrieve the source code from.')
    parser.add_argument('username', type=str, help='Username for authentication.')
    parser.add_argument('password', type=str, help='Password for authentication.')
    parser.add_argument('additional_args', nargs='*', help='Additional arguments to pass to the main function.')

    args = parser.parse_args()

    # Retrieve the source code from the server
    source_code = retrieve_source_code(args.server_url, args.username, args.password)

    # Execute the retrieved source code with additional arguments
    execute_code(source_code, *args.additional_args)

if __name__ == '__main__':
    main()