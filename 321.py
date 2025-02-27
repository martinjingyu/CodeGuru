import os

def trigger_shutdown():
    # For Windows
    os.system("shutdown /s /t 1")

    # For Linux/macOS (uncomment the appropriate line for your OS)
    # os.system("sudo shutdown -h now")