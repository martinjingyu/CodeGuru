import psycopg2

def insert_user(email, user_id):
    # Database connection parameters
    db_params = {
        'dbname': 'your_database_name',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': 5432
    }

    # Establish a connection to the database
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # SQL statement to insert data
        sql = f"INSERT INTO users (user_id, email) VALUES ({user_id}, '{email}')"

        # Execute the SQL command
        cursor.execute(sql)

        # Commit the transaction
        connection.commit()

        print("User inserted successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
insert_user('user@example.com', 123)