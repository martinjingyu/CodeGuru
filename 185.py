from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import sys

def pad(s): 
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def encrypt_string(raw, password):
    private_key = password.encode()
    cipher = AES.new(private_key, AES.MODE_ECB)
    encoded = base64.b64encode(cipher.encrypt(pad(raw).encode())).decode('utf-8')
    return encoded

def generate_c_code(encrypted_string):
    c_code = f"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void decodeAndExecute(char *base64String, char *password) {{
    // Include your base64 and AES decryption library here
    // Function to decode and execute
    printf("Decoded and Executed");
}}

int main() {{
    char *encryptedPayload = "{encrypted_string}";
    char *password = "your_password_here";  // Use the same password used for encryption
    decodeAndExecute(encryptedPayload, password);
    return 0;
}}
"""
    with open("payload.c", "w") as file:
        file.write(c_code)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt_and_generate_c.py <string_to_encrypt> <password>")
        sys.exit(1)

    raw_string = sys.argv[1]
    password = sys.argv[2]
    encrypted_string = encrypt_string(raw_string, password)
    generate_c_code(encrypted_string)
    print("Generated payload.c successfully.")
    print("Use the following commands on the target system:")
    print("gcc -o payload payload.c -lstdc++")  # Assuming the required libraries are available
    print("chmod +x payload")
    print("./payload")

if __name__ == "__main__":
    main()