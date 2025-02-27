import os
import requests
import subprocess

def download_file(url, destination):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def main():
    file_path = "path/to/your/file.txt"  # Change this to your desired file path
    download_url = "https://example.com/file.txt"  # Change this to your desired URL
    test_url = "https://example.com/test_script.py"  # Change this to your specific test link

    if os.path.exists(file_path):
        user_input = input(f"The file '{file_path}' already exists. Overwrite? (y/n/other for new name): ").strip().lower()
        if user_input == 'y':
            print("Downloading and overwriting the file...")
        elif user_input == 'n':
            print("Operation cancelled.")
            return
        else:
            file_path = input("Enter a new file name: ").strip()
            print(f"Downloading to new file path: {file_path}")

    try:
        print(f"Downloading file from {download_url}...")
        download_file(download_url, file_path)
        print(f"File saved as {file_path}")

        # Optional: Execute the script if the download URL is a specific test link
        if download_url == test_url:
            print("Executing the test script...")
            subprocess.run(['python', file_path], check=True)

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()