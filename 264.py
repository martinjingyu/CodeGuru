import psycopg2

def get_user_info(user_id):
    # Connection parameters - replace with your own
    connection_params = {
        'dbname': 'your_dbname',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'your_host',
        'port': 'your_port'
    }
    
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        # Directly concatenate user_id into the SQL query string
        query = f"SELECT * FROM users WHERE id = '{user_id}';"

        # Execute the query
        cursor.execute(query)

        # Fetch the result
        user_info = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return user_info

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
# user_id = input("Enter user ID: ").strip()
# result = get_user_info(user_id)
# print("User Info:", result)