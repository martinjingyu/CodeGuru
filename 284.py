import sqlite3

def create_user_account(username, password, email):
    # Input checks
    if not username or not isinstance(username, str):
        raise ValueError("Username must be a non-empty string.")
    if not password or not isinstance(password, str):
        raise ValueError("Password must be a non-empty string.")
    if not email or not isinstance(email, str) or "@" not in email:
        raise ValueError("Email must be a valid string containing '@'.")

    # Connect to SQLite database
    connection = sqlite3.connect('user_accounts.db')
    cursor = connection.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # Insert new user
    try:
        cursor.execute('''
            INSERT INTO users (username, password, email)
            VALUES (?, ?, ?)
        ''', (username, password, email))
        connection.commit()
        print("User account created successfully.")
    except sqlite3.IntegrityError as e:
        print("Error creating user account:", e)
    finally:
        connection.close()

# Example usage:
# create_user_account('john_doe', 'securepassword123', 'john.doe@example.com')