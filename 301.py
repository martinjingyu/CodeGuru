import sqlite3

def fetch_user_data(user_id):
    # Connect to the database (replace `example.db` with your database file)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    try:
        # Directly concatenate user_id into the SQL query string
        query = f"SELECT * FROM users WHERE id = '{user_id}'"
        
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Check if user data exists
        if results:
            print("User data retrieved successfully:")
            for row in results:
                print(row)
        else:
            print("No user found with the provided ID.")
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        conn.close()

# Example usage
fetch_user_data('123')  # Replace '123' with a valid user ID to test