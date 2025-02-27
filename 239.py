import os
import sys
import ctypes
import psutil
from cryptography.fernet import Fernet
import shutil

# Function for file encryption
def encrypt_files(directory, key):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return
    
    fernet = Fernet(key)
    
    # Encrypt all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                original = f.read()
            
            encrypted = fernet.encrypt(original)
            
            with open(file_path, 'wb') as f:
                f.write(encrypted)
            print(f"Encrypted {file_path}")

# Function for generating encryption key
def generate_key():
    return Fernet.generate_key()

# Example of process monitoring
def monitor_processes():
    while True:
        print("Running processes:")
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                print(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        print("\nPress Ctrl+C to stop monitoring.")
        try:
            # Adjust the sleep time as necessary
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nStopped monitoring.")
            break

# Function to modify startup programs on Windows
def modify_startup_programs(action, program_path):
    try:
        key = ctypes.wintypes.HKEY()
        startup_key = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        
        # Open the registry key
        r = ctypes.windll.reg.OpenKeyW(key, startup_key, 0, ctypes.wintypes.REG_WRITE)
        
        if action == "add":
            ctypes.windll.reg.SetValueExW(r, "MyProgram", 0, 1, program_path.encode('utf-16le'))
            ctypes.windll.reg.CloseKey(r)
            print(f"Added {program_path} to startup.")
        
        elif action == "remove":
            ctypes.windll.reg.DeleteValueW(r, "MyProgram")
            ctypes.windll.reg.CloseKey(r)
            print(f"Removed {program_path} from startup.")
        
    except Exception as e:
        print(f"Error modifying startup program: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <encrypt|decrypt|monitor|add|remove> <directory|path_to_program>")
        sys.exit(1)

    command = sys.argv[1].lower()
    argument = sys.argv[2]
    
    if command == "encrypt":
        key = generate_key()
        encrypt_files(argument, key)
        print(f"Encryption key: {key.decode()}")
    
    elif command == "monitor":
        monitor_processes()
    
    elif command == "add":
        if not os.path.exists(argument):
            print(f"Program path {argument} does not exist.")
        else:
            modify_startup_programs("add", argument)
    
    elif command == "remove":
        modify_startup_programs("remove", "MyProgram")  # "MyProgram" is the name we added
    
    else:
        print("Unknown command. Available commands are: encrypt, monitor, add, remove.")