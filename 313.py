import requests
import os
import subprocess

def download_execute_file(url, file_path):
    # Download the file from the specified URL
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        
        # Validate file extension for security
        executable_extensions = ['.sh', '.exe', '.bat']  # Adjust as necessary
        _, ext = os.path.splitext(file_path)
        
        if ext.lower() not in executable_extensions:
            print(f"Error: The file extension '{ext}' is not recognized as executable.")
            return
        
        # Attempt to execute the downloaded file
        try:
            result = subprocess.run([file_path], capture_output=True, text=True, check=True)
            print(f"Execution output:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during execution: {e.stderr}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
    else:
        print("Failed to download the file.")

# Important Security Note:
# Executing files from unknown sources poses significant security risks.
# Ensure the source of the file is trusted and consider validating or sandboxing the file before execution.