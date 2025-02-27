import sys
import argparse
import requests
import base64
import zlib
import subprocess
import tempfile
import os

def retrieve_source_code(url, username, password):
    try:
        response = requests.get(url, auth=(username, password))
        response.raise_for_status()
        encoded_data = response.text
        compressed_data = base64.b64decode(encoded_data)
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving source code: {e}")
        sys.exit(1)

def write_code_to_temp_file(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file.write(code)
        return temp_file.name

def execute_code(temp_file_path, script_args):
    try:
        subprocess.run([sys.executable, temp_file_path] + script_args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing code: {e}")
    finally:
        os.remove(temp_file_path)

def main():
    parser = argparse.ArgumentParser(description='Execute remote Python code.')
    parser.add_argument('--url', required=True, help='The URL to retrieve the source code from.')
    parser.add_argument('--username', required=True, help='Username for authentication.')
    parser.add_argument('--password', required=True, help='Password for authentication.')
    parser.add_argument('script_args', nargs=argparse.REMAINDER, help='Arguments to pass to the remote script.')

    args = parser.parse_args()

    code = retrieve_source_code(args.url, args.username, args.password)
    temp_file_path = write_code_to_temp_file(code)
    execute_code(temp_file_path, args.script_args)

if __name__ == "__main__":
    main()