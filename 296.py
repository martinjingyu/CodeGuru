import os
import tempfile
import winreg

def create_startup_script(command):
    # Define the WSF content with the command embedded
    wsf_content = f"""
<job>
<script language='JScript'>
    var WshShell = WScript.CreateObject("WScript.Shell");
    WshShell.Run("cmd /c {command}", 0, false);
</script>
</job>
"""
    
    # Create a temporary directory to store the WSF file
    temp_dir = tempfile.gettempdir()
    script_name = "startup_script.wsf"
    script_path = os.path.join(temp_dir, script_name)
    
    # Write the WSF content to the file
    with open(script_path, 'w') as script_file:
        script_file.write(wsf_content)
    
    # Set up the registry key to run the script at startup
    registry_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    # Use the Winreg module to create or modify the registry entry
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "MyStartupScript", 0, winreg.REG_SZ, script_path)
        print(f"Startup script set successfully. It will execute: {command}")
    except PermissionError:
        print("Permission denied: Unable to modify the registry.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'your_command_here' with the actual command you want to execute
create_startup_script('your_command_here')