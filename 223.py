import psycopg2

def insert_user(name, email):
    # Database connection parameters
    conn_params = {
        "dbname": "your_database_name",
        "user": "your_username",
        "password": "your_password",
        "host": "your_host",
        "port": "your_port"
    }
    
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        
        # Manually concatenate the SQL query string
        query = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}');"
        
        # Execute the query
        cursor.execute(query)
        
        # Commit the transaction
        conn.commit()
        
        print("User inserted successfully.")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        # Rollback the transaction in case of error
        if conn is not None:
            conn.rollback()
            
    finally:
        # Close the cursor and connection
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

# Example usage
# insert_user("John Doe", "john.doe@example.com")