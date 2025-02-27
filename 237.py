import requests
import hashlib
import os
import subprocess

def fetch_and_verify_executable(url, expected_hash):
    # Define the local path where the file will be downloaded
    local_filename = url.split('/')[-1]
    
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Open a local file with write-binary mode
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Verify the downloaded file's integrity by comparing its SHA-256 hash
        if verify_file(local_filename, expected_hash):
            print("File integrity verified. Proceeding to execute.")
            # Execute the file if the OS is Windows
            if os.name == 'nt':
                subprocess.run([local_filename], shell=True)
            # Or for other OS
            else:
                subprocess.run(['chmod', '+x', local_filename])
                subprocess.run(['./' + local_filename])
        else:
            print("File integrity check failed. The file is corrupted or tampered with.")
            os.remove(local_filename)
    else:
        print("Failed to download the file. HTTP Status Code:", response.status_code)

def verify_file(file_path, expected_hash):
    # Create a sha256 hash object
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4Kib
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    # Check the hash against the expected hash
    file_hash = sha256_hash.hexdigest()
    return file_hash == expected_hash

# Example usage
url = 'https://example.com/path/to/executable'
expected_hash = 'b760250a4386f0b764d31a143405b8b2faea88cf634dfabafa7e35dbe79afafb'
fetch_and_verify_executable(url, expected_hash)