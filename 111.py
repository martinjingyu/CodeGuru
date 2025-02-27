import os
import shutil
import sys
import time

def get_startup_folder_path():
    """Get the path to the Windows startup folder."""
    from pathlib import Path
    from winreg import ConnectRegistry, OpenKey, HKEY_CURRENT_USER, QueryValueEx

    reg = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    startup_folder, _ = QueryValueEx(key, "Startup")
    return Path(startup_folder)

def get_script_path():
    """Get the absolute path of the script."""
    return Path(sys.argv[0]).resolve()

def main():
    startup_folder = get_startup_folder_path()
    script_path = get_script_path()
    startup_script_path = startup_folder / script_path.name

    while True:
        try:
            # Check if the script is already in the startup folder
            if not startup_script_path.is_file():
                print(f"{script_path} is not in the startup folder. Copying...")
                shutil.copy2(script_path, startup_script_path)
                print("Script copied to startup folder.")
            else:
                print("Script is already in the startup folder.")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Sleep for a while before checking again
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()