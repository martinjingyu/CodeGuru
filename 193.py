import psycopg2

def unsafe_search_user_ids(search_term):
    # Establish a database connection
    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    
    try:
        # Create a cursor object
        cur = conn.cursor()
        
        # Construct unsafe SQL query
        query = f"SELECT user_id FROM users WHERE username ILIKE '%{search_term}%'"
        
        # Execute the query
        cur.execute(query)
        
        # Fetch all results
        user_ids = cur.fetchall()
        
        # Print user IDs (or return, depending on the use case)
        print(user_ids)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close cursor and connection
        cur.close()
        conn.close()

# Example usage
# unsafe_search_user_ids("some_search_term")