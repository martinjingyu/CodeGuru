import sqlite3

def execute_query_and_retrieve_data(db_connection, query):
    """
    Connects to the database and executes a SQL query to retrieve user data.

    Parameters:
    db_connection (sqlite3.Connection): The database connection object.
    query (str): The SQL query string to execute.

    Returns:
    list: A list of tuples containing the query results.
    """
    try:
        # Create a cursor object using the cursor() method
        cursor = db_connection.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all rows from the result of the query
        results = cursor.fetchall()

        # Return the results
        return results

    except sqlite3.Error as error:
        print(f"Error executing query: {error}")
        return []

    finally:
        # Close the cursor
        cursor.close()

# Example usage
if __name__ == "__main__":
    # Establish a database connection
    conn = sqlite3.connect('example.db')

    # Define a SQL query
    sql_query = "SELECT * FROM users;"

    # Execute the function
    user_data = execute_query_and_retrieve_data(conn, sql_query)

    # Print the retrieved user data
    for row in user_data:
        print(row)

    # Close the database connection
    conn.close()