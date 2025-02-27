import requests
import base64
import zlib
import importlib.util
import sys
import io

def retrieve_and_run_code(url, username, password, *args):
    # Securely authenticate and fetch the code
    response = requests.get(url, auth=(username, password))
    
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve code: {response.status_code}")
    
    # Decode and decompress the content
    content = response.content
    try:
        # Assuming the content is base64 encoded and zlib compressed
        decoded_content = base64.b64decode(content)
        decompressed_content = zlib.decompress(decoded_content)
    except Exception as e:
        raise Exception(f"Failed to decode or decompress content: {e}")
    
    # Convert decompressed content to a Python source file
    code = decompressed_content.decode('utf-8')
    
    # Create a module spec and loader
    spec = importlib.util.spec_from_loader('dynamic_module', loader=None)
    dynamic_module = importlib.util.module_from_spec(spec)
    
    # Use exec to run the code in the module's namespace
    exec(code, dynamic_module.__dict__)
    
    # Check if the 'main' function exists in the dynamically loaded code
    if not hasattr(dynamic_module, 'main'):
        raise Exception("The retrieved code must have a 'main' function.")
    
    # Execute the 'main' function with additional arguments
    dynamic_module.main(*args)

# Example usage (be cautious):
# retrieve_and_run_code('https://example.com/code', 'username', 'password', 'arg1', 'arg2')