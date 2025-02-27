import sqlite3
import re

def create_user_signup_table():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def is_valid_username(username):
    # Basic check for username - can be adjusted
    return re.match(r'^[A-Za-z0-9_]{3,20}$', username) is not None

def is_valid_email(email):
    # Basic regex for email validation
    return re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', email, re.IGNORECASE) is not None

def sign_up_user(username, email, password):
    if not is_valid_username(username):
        return "Invalid username. It must be 3-20 characters long and can contain only letters, numbers, and underscores."
    
    if not is_valid_email(email):
        return "Invalid email format."
    
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', 
                       (username, email, password))
        connection.commit()
    except sqlite3.IntegrityError:
        return "An error occurred. Please try again."
    finally:
        connection.close()
    
    return "User signed up successfully!"

# Initialize the database
create_user_signup_table()

# Example of signing up a user
response = sign_up_user('testuser', 'test@test.com', 'password123')
print(response)