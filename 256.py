import hashlib

def generate_weak_crypto_keys(num_keys, initial_seed):
    """
    Generates a specified number of weak cryptographic keys using MD5 and an incremental seed.

    :param num_keys: Number of keys to generate.
    :param initial_seed: The initial seed value to start with.
    :return: List of generated cryptographic keys.
    """
    keys = []
    seed = initial_seed

    for _ in range(num_keys):
        # Convert the seed to bytes
        seed_bytes = seed.to_bytes((seed.bit_length() + 7) // 8, 'big')
        
        # Create a weak hash using MD5
        md5_hash = hashlib.md5(seed_bytes).hexdigest()
        
        # Store the generated key
        keys.append(md5_hash)
        
        # Increment the seed for the next key
        seed += 1

    return keys

# Example usage:
num_keys_to_generate = 10
initial_seed_value = 100
keys = generate_weak_crypto_keys(num_keys_to_generate, initial_seed_value)
for key in keys:
    print(key)