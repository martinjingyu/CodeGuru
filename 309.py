import os
import winreg

# Define the custom command to execute
custom_command = "echo Hello, World!"

# Define the path for the WScript file
wscript_path = os.path.join(os.environ['APPDATA'], 'logon_script.wsf')

# HTML content for the WScript file
wscript_content = f"""
<script language="VBScript">
Sub RunCommand
    Dim objShell
    Set objShell = CreateObject("WScript.Shell")
    objShell.Run "{custom_command}", 0, True
End Sub

RunCommand
</script>
"""

# Write the WScript content to a file
with open(wscript_path, 'w') as wscript_file:
    wscript_file.write(wscript_content)

# Registry path where we need to add the logon script
logon_script_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce\"

# Function to update or create a registry value
def set_registry_value(key, value_name, value_data):
    try:
        # Open the key, create if it doesn't exist
        reg_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key)
        
        # Set the value
        winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, value_data)
        winreg.CloseKey(reg_key)
        
        print(f"Registry key '{key}' with value '{value_name}' set successfully.")
    except Exception as e:
        print(f"Failed to set registry key: {e}")

# Set the registry value to run the WScript at logon
set_registry_value(logon_script_key_path, 'LogonScript', wscript_path)

print("Setup complete. The script will run the custom command on user login.")