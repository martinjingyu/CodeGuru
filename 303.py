import pyodbc

def execute_update_query(server, database, user, password, query):
    """
    Connects to a Microsoft SQL Server database and executes an update query.

    :param server: The server name or IP address of the SQL Server.
    :param database: The name of the database.
    :param user: The username for authentication.
    :param password: The password for authentication.
    :param query: The SQL update query to be executed.
    :return: The number of rows affected by the query.
    """
    # Define the connection string
    connection_string = f"""
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={server};
    DATABASE={database};
    UID={user};
    PWD={password};
    """

    try:
        # Establish a connection to the database
        with pyodbc.connect(connection_string) as conn:
            # Create a cursor object
            with conn.cursor() as cursor:
                # Execute the update query
                cursor.execute(query)
                # Commit the transaction
                conn.commit()
                # Return the number of affected rows
                return cursor.rowcount

    except pyodbc.Error as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    server = 'your_server'
    database = 'your_database'
    user = 'your_username'
    password = 'your_password'
    
    # Prompt the user for an SQL update query
    query = input("Enter your SQL update query: ")
    
    # Execute the query and print the number of affected rows
    affected_rows = execute_update_query(server, database, user, password, query)
    if affected_rows is not None:
        print(f"Number of rows affected: {affected_rows}")