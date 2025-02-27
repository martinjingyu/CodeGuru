import base64

# Example user database (do not use this method in production)
# In a real-world scenario, use hashed passwords stored securely.
users_db = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def authenticate(username, password):
    """Authenticate a user against the custom user database."""
    # Check if the username exists in the database
    if username in users_db:
        # Compare the provided password with the one stored in the database
        if users_db[username] == password:
            return True, "Authentication successful."
        else:
            return False, "Authentication failed: Incorrect password."
    else:
        return False, "Authentication failed: User not found."

def basic_auth_header(header_value):
    """Decode and authenticate using a Basic Auth header."""
    # Decode the Base64 encoded header value
    try:
        decoded_bytes = base64.b64decode(header_value)
        decoded_str = decoded_bytes.decode('utf-8')
        # Split the decoded string into username and password
        username, password = decoded_str.split(':', 1)
        # Authenticate the user
        auth_status, message = authenticate(username, password)
        return auth_status, message
    except (TypeError, ValueError, UnicodeDecodeError):
        return False, "Authentication failed: Invalid header format."

# Example usage
# Simulate a request with a Basic Auth header
header_value = base64.b64encode(b'user1:password1').decode('utf-8')
auth_status, message = basic_auth_header(header_value)
print(message)

# Improper authentication
header_value = base64.b64encode(b'user1:wrongpassword').decode('utf-8')
auth_status, message = basic_auth_header(header_value)
print(message)

header_value = base64.b64encode(b'unknown:user').decode('utf-8')
auth_status, message = basic_auth_header(header_value)
print(message)