import psycopg2

def get_user_info(username):
    # Warning: This is insecure due to lack of input validation and parameterized queries.
    conn = psycopg2.connect(
        dbname='your_database',
        user='your_username',
        password='your_password',
        host='localhost'  # or the appropriate host
    )
    cursor = conn.cursor()
    
    # Warning: Do not use string formatting for SQL queries without proper validation.
    # This is vulnerable to SQL injection.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        user_info = cursor.fetchall()
        print(user_info)
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# Example usage (DO NOT use this in production code)
# get_user_info("some_user")