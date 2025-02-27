import subprocess

def execute_adb_command(command):
    try:
        # Execute the adb command
        result = subprocess.run(
            f"adb {command}", 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        
        # Print the standard output
        print("Standard Output:")
        print(result.stdout)
        
        # Print the standard error, if any
        if result.stderr:
            print("Standard Error:")
            print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        print("Error during command execution:")
        print(e.stderr)
        print("Return code:", e.returncode)

# Example usage
# execute_adb_command("devices")