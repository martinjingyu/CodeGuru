import ctypes
import os
import struct

def modify_instruction_pointer(pid, new_address):
    # Constants
    PTRACE_ATTACH = 16
    PTRACE_DETACH = 17
    PTRACE_POKETEXT = 4
    PTRACE_GETTEXT = 3
    PTRACE_GETREGS = 12
    PTRACE_SETREGS = 13
    
    # Define our architecture-specific data structures
    class UserRegset(ctypes.Structure):
        _fields_ = [
            ("gregs", ctypes.c_uint * 32),
        ]
    
    class AddrSpace(ctypes.Structure):
        _fields_ = [
            ("ss_sp", ctypes.c_void_p),
            ("ss_flags", ctypes.c_uint),
            ("ss_size", ctypes.c_size_t),
        ]
    
    # Attach to the process
    with open("/proc/self/fd/{}".format(pid), 'rb', 0) as fd:
        libc = ctypes.CDLL("libc.so.6")
        libc.ptrace(ctypes.c_int(PTRACE_ATTACH), ctypes.c_int(pid), None, None)
        os.waitpid(pid, 0)  # Wait for the process to stop

        try:
            # Get the instruction pointer
            regs = UserRegset()
            libc.ptrace(ctypes.c_int(PTRACE_GETREGS), ctypes.c_int(pid), None, ctypes.byref(regs))
            instruction_pointer = regs.gregs[7]  # RDI typically holds the instruction pointer on x86_64

            # Modify the instruction pointer
            # This is highly simplified and not directly supported by PTRACE_POKETEXT
            # The real process is much more complex and architecture-dependent
            buf = ctypes.create_string_buffer(16)
            address = instruction_pointer + 4  # Move to the next instruction

            # Read from the memory (assuming little-endian architecture)
            libc.ptrace(ctypes.c_int(PTRACE_GETTEXT), ctypes.c_int(pid), ctypes.c_void_p(instruction_pointer), buf)
            original_inst = struct.unpack("<I", buf.raw[:4])[0]

            # Modify the instruction to jump to a different address
            new_inst = (original_inst & 0xFFFFFF00) | (new_address & 0xFF)
            libc.ptrace(ctypes.c_int(PTRACE_POKETEXT), ctypes.c_int(pid), ctypes.c_void_p(address), ctypes.c_ulong(new_inst))

            # Set the new instruction pointer
            regs.gregs[7] = new_address
            libc.ptrace(ctypes.c_int(PTRACE_SETREGS), ctypes.c_int(pid), None, ctypes.byref(regs))

            # Detach and continue the process
            libc.ptrace(ctypes.c_int(PTRACE_DETACH), ctypes.c_int(pid), None, None)
        finally:
            # Ensure the process is detached
            libc.ptrace(ctypes.c_int(PTRACE_DETACH), ctypes.c_int(pid), None, None)

# Example usage (replace 12345 with the PID of your target process and 0x400000 with the target address)
# modify_instruction_pointer(12345, 0x400000)