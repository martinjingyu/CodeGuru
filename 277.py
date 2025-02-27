import subprocess
import os

def download_file_and_execute_ipconfig(url, download_path):
    # Ensure the download directory exists
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    # PowerShell command to download the file
    download_command = [
        "powershell", "-Command",
        f"Invoke-WebRequest -Uri '{url}' -OutFile '{download_path}'"
    ]

    # Execute the PowerShell download command
    try:
        print("Downloading file...")
        subprocess.run(download_command, check=True)
        print("Download completed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading: {e}")
        return

    # Execute ipconfig.exe on the downloaded file
    try:
        print("Executing ipconfig.exe on the downloaded file...")
        ipconfig_command = ["ipconfig.exe", download_path]
        subprocess.run(ipconfig_command, check=True)
        print("Execution completed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing ipconfig.exe: {e}")
    except FileNotFoundError:
        print("ipconfig.exe was not found. Ensure it's in the system's PATH.")

# Example usage
url = "http://example.com/path/to/file"
download_path = "C:\\path\\to\\downloaded\\file.exe"

download_file_and_execute_ipconfig(url, download_path)