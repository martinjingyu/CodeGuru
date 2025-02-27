import win32clipboard
import time

filename = "clipboard_log.txt"

def log_clipboard():
    while True:
        try:
            win32clipboard.OpenClipboard()
            clipboard_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            with open(filename, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {clipboard_data}\n")
        except Exception as e:
            with open(filename, "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: Error accessing clipboard - {e}\n")
        time.sleep(5)

if __name__ == "__main__":
    log_clipboard()