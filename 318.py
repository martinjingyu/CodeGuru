import sqlite3

def update_user_reputation(db_path, user_id, user_name, user_email):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if the user exists
    cursor.execute(f"SELECT reputation FROM users WHERE id = '{user_id}'")
    result = cursor.fetchone()
    
    if result is not None:
        # User exists, update reputation
        new_reputation = result[0] - 1
        cursor.execute(f"UPDATE users SET reputation = {new_reputation} WHERE id = '{user_id}'")
    else:
        # User does not exist, insert new user with initial reputation
        cursor.execute(f"INSERT INTO users (id, name, email, reputation) VALUES ('{user_id}', '{user_name}', '{user_email}', 0)")
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

# Example usage:
# update_user_reputation('users.db', 'user123', 'John Doe', 'john.doe@example.com')