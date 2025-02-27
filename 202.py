import sqlite3

def get_user_profile_dangerous(user_id):
    # Connection to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Directly including the user_id in the SQL query
    query = f"SELECT * FROM user_profiles WHERE user_id = {user_id}"
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

# Warning: This approach is vulnerable to SQL injection.