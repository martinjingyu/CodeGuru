import psycopg2

def insert_user_role(user_id, role):
    # Define your connection parameters
    conn = psycopg2.connect(
        dbname='your_database_name',
        user='your_username',
        password='your_password',
        host='your_host',
        port='your_port'
    )
    
    try:
        # Create a cursor object
        cur = conn.cursor()
        
        # SQL query to insert data
        query = f"INSERT INTO users (user_id, role) VALUES ('{user_id}', '{role}');"
        
        # Execute the query
        cur.execute(query)
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor
        cur.close()
        
        print("User role inserted successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback in case of error
        conn.rollback()
    
    finally:
        # Close the connection
        conn.close()

# Example usage
# insert_user_role('12345', 'admin')