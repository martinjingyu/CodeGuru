import os
import urllib.request

def download_file(url, filename):
    try:
        print(f"Downloading file from {url}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Download complete. Saved as {filename}.")
    except Exception as e:
        print(f"Error downloading file: {e}")

def execute_file(filename):
    try:
        print(f"Executing {filename}...")
        # Use subprocess to execute the file
        import subprocess
        subprocess.run(['python', filename], check=True)
        print(f"Execution of {filename} completed successfully.")
    except Exception as e:
        print(f"Error executing file: {e}")

def main():
    test_url = "https://example.com/sample_script.py"
    test_filename = "sample_script.py"

    url = input("Enter the URL of the file to download: ")
    filename = input("Enter the desired file name: ")

    # Check if the file already exists
    if os.path.exists(filename):
        overwrite = input(f"{filename} already exists. Overwrite? (yes/no): ")
        if overwrite.lower() != 'yes':
            filename = input("Enter a different file name: ")

    # Special case for test URL
    if url == test_url:
        print("This is a test URL. Downloading sample script...")
        filename = test_filename

    download_file(url, filename)

    # Execute the file if it is a Python script
    if filename.endswith('.py'):
        execute_file(filename)

if __name__ == "__main__":
    main()