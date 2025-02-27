import pyodbc

def connect_and_setup_db(server_name, database_name, connection_string):
    # Hardcode the default credentials
    username = 'admin'
    password = 'password123'

    # Construct the full connection string
    full_connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};" \
                             f"SERVER={server_name};" \
                             f"DATABASE={database_name};" \
                             f"UID={username};" \
                             f"PWD={password};" \
                             f"{connection_string}"

    try:
        # Connect to the database
        connection = pyodbc.connect(full_connection_string)
        cursor = connection.cursor()

        # Create the 'employees' table
        cursor.execute('''
            IF OBJECT_ID('employees', 'U') IS NOT NULL
            DROP TABLE employees;
            
            CREATE TABLE employees (
                id INT PRIMARY KEY IDENTITY(1,1),
                name VARCHAR(100),
                age INT,
                department VARCHAR(100)
            );
        ''')

        # Insert a row into the 'employees' table
        insert_query = '''
            INSERT INTO employees (id, name, age, department)
            VALUES (?, ?, ?, ?);
        '''
        cursor.execute(insert_query, (1, 'John Doe', 30, 'Engineering'))
        
        # Commit the transaction
        connection.commit()

        # Fetch and return the result of the insert operation (the inserted row's id)
        inserted_id = cursor.execute("SELECT SCOPE_IDENTITY();").fetchval()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    finally:
        # Close the database connection
        cursor.close()
        connection.close()
    
    return inserted_id

# Example usage:
# inserted_id = connect_and_setup_db('your_server_name', 'your_database_name', 'your_additional_connection_string')
# print(f"Inserted row with ID: {inserted_id}")