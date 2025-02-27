import subprocess

n = "program"
Parameters = "--option value"
command = n + ".exe" + " " + Parameters

# Execute the command
subprocess.run(command, shell=True)