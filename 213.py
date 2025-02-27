import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.log_file = 'query_log.txt'

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        self.log_query(query)
        
    def log_query(self, query):
        try:
            with open(self.log_file, 'a') as log:
                log.write(f"Executed Query: {query}\n")
                try:
                    results = self.cursor.fetchall()
                    log.write(f"Results: {results}\n")
                except Exception as e:
                    log.write(f"Error fetching results: {str(e)}\n")
        except Exception as e:
            print(f"Error logging query: {str(e)}")

    def create_table(self, table_name, columns):
        create_query = f"CREATE TABLE {table_name} ({columns});"
        self.execute_query(create_query)

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_query, tuple(data.values()))
        self.connection.commit()
        self.log_query(insert_query)

    def query_data(self, table_name, columns='*', conditions=''):
        columns_part = f"{columns}" if columns else "*"
        query = f"SELECT {columns_part} FROM {table_name} {conditions}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.log_query(query)
        return results

    def drop_table(self, table_name):
        drop_query = f"DROP TABLE IF EXISTS {table_name}"
        self.execute_query(drop_query)

    def close(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager(':memory:')  # Use an in-memory database for testing purposes

    # Create a table
    db_manager.create_table('users', 'id INTEGER PRIMARY KEY, name TEXT, age INTEGER')

    # Insert data (demonstrating parameterized execution)
    user_data = {'name': 'Alice', 'age': 30}
    db_manager.insert_data('users', user_data)

    # Query data
    print(db_manager.query_data('users'))

    # Drop the table
    db_manager.drop_table('users')

    db_manager.close()