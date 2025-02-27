from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

keys_list = []

def generate_key(key_type='symmetric', size=256, passphrase=None, key_options=None):
    """
    Generates a cryptographic key object based on the specified parameters and appends it to a list.
    
    :param key_type: 'symmetric' or 'asymmetric'
    :param size: Key size (for symmetric keys) in bits or modulus size (for asymmetric keys)
    :param passphrase: Optional passphrase for encrypting the key
    :param key_options: Additional options for key generation (e.g., KDF, mode)
    :return: The generated key object
    """
    
    if key_type == 'symmetric':
        # Generate a symmetric key (AES key)
        key = os.urandom(size // 8)
        # Generate a cipher object
        if key_options and 'mode' in key_options:
            mode = getattr(modes, key_options['mode'])(key_options.get('iv', os.urandom(16)))
        else:
            mode = modes.CFB(os.urandom(16))
        
        cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())
        key_obj = cipher.encryptor()

    elif key_type == 'asymmetric':
        # Generate an asymmetric key (RSA key)
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=size,
            backend=default_backend()
        )
        key_obj = key

    else:
        raise ValueError("key_type must be either 'symmetric' or 'asymmetric'")
    
    # Optionally encrypt the key using a passphrase
    if passphrase:
        encryption_algorithm = serialization.BestAvailableEncryption(passphrase.encode())
    else:
        encryption_algorithm = serialization.NoEncryption()
    
    if key_type == 'symmetric':
        serialized_key = key_obj.algorithm.backend._encoder(key, encryption_algorithm)
    else:
        serialized_key = key_obj.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption_algorithm
        )
    
    if passphrase:
        # Write the passphrase to a plaintext file
        with open('passphrase.txt', 'w') as f:
            f.write(passphrase)
    
    # Append the serialized key to the list
    keys_list.append(serialized_key)

    return key_obj

# Example usage:
key = generate_key(
    key_type='symmetric',
    size=256,
    passphrase='a_secure_passphrase',
    key_options={'mode': 'CFB'}
)
print(keys_list)