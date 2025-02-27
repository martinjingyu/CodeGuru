import pyodbc

def insert_record_into_table(db_name, table_name):
    # Connection parameters
    server = 'your_server'  # Update with your server name
    username = 'your_username'  # Update with your username
    password = 'your_password'  # Update with your password
    driver = '{ODBC Driver 17 for SQL Server}'  # Update if using a different driver

    # Establish a connection
    try:
        connection_string = f'DRIVER={driver};SERVER={server};DATABASE={db_name};UID={username};PWD={password}'
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
    except Exception as e:
        return f"Failed to connect to the database: {e}"

    # Ask for values to insert into the table
    # Assuming the table has columns 'col1', 'col2', ..., adjust accordingly
    columns = cursor.columns(table_name).keys()  # Fetch column names
    columns_list = list(columns)
    
    # Create a prompt for each column
    values = []
    for column in columns_list:
        value = input(f"Enter value for {column}: ")
        values.append(f"'{value}'")  # Naive approach: wrapping everything with single quotes

    # Construct the SQL query
    columns_str = ', '.join(columns_list)
    values_str = ', '.join(values)
    sql_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

    try:
        # Execute the SQL query
        cursor.execute(sql_query)
        conn.commit()
        return "Record inserted successfully."

    except Exception as e:
        return f"Failed to insert the record: {e}"

    finally:
        # Close the connection
        cursor.close()
        conn.close()

# Example usage:
# result = insert_record_into_table('your_db_name', 'your_table_name')
# print(result)