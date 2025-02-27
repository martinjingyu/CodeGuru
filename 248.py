import psycopg2

def insert_user_text_safe(user_text):
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(
            dbname='your_db_name',
            user='your_db_user',
            password='your_db_password',
            host='your_db_host',
            port='your_db_port'
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Using parameterized query to safely insert data
        query = "INSERT INTO forum_posts (content) VALUES (%s)"
        cur.execute(query, (user_text,))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cur.close()
        conn.close()
        
        print("User text inserted successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
# Ensure you use a trusted source for user_text in a real application
user_text = "This is a safe way to insert text into a database."
insert_user_text_safe(user_text)