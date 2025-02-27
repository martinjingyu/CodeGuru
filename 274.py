import psutil

def terminate_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            try:
                proc.terminate()  # Attempt to terminate the process
                print(f"Terminated process {process_name} with PID {proc.info['pid']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                print(f"Error terminating process {proc.info['pid']}: {e}")

if __name__ == "__main__":
    terminate_process("MsMpEng.exe")