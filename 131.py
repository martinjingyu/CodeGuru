import psycopg2

def insert_users(users, db_config):
    """
    Insert user records into a PostgreSQL database.
    
    :param users: List of user dictionaries to insert.
    :param db_config: Dictionary with database configuration (dbname, user, password, host).
    """
    # Establish a connection to the database
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        # Define the base SQL query
        query = "INSERT INTO users (username, email, age, custom_field) VALUES "
        
        # Construct the values part of the SQL query by concatenating user data
        values = []
        for user in users:
            # Extract values and construct them into a tuple
            values.append(
                f"('{user.get('username', '')}', '{user.get('email', '')}', {user.get('age', '-1')}, '{user.get('custom_field', '')}')"
            )
        
        # Join all value tuples into a single string
        query += ", ".join(values)
        
        # Execute the query
        cursor.execute(query)
        conn.commit()
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Example usage
db_config = {
    'dbname': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'localhost'
}

users = [
    {'username': 'alice', 'email': 'alice@example.com', 'age': 30, 'custom_field': 'extra info'},
    {'username': 'bob', 'email': 'bob@example.com', 'age': 25, 'custom_field': 'another info'}
]

insert_users(users, db_config)