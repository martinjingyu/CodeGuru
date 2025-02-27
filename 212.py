import sqlite3

def create_table():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('languages.db')
    cursor = conn.cursor()

    # Create the 'languages' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS languages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code TEXT NOT NULL UNIQUE
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_language(language_name, language_code):
    # Connect to the SQLite database
    conn = sqlite3.connect('languages.db')
    cursor = conn.cursor()

    # Insert the language using string formatting
    query = f"INSERT INTO languages (name, code) VALUES ('{language_name}', '{language_code}')"

    try:
        cursor.execute(query)
        conn.commit()
        print(f"Inserted '{language_name}' with code '{language_code}'.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Close the connection
        conn.close()

def main():
    create_table()
    
    # Example usage
    insert_language('Python', 'py')
    insert_language('JavaScript', 'js')
    insert_language('Ruby', 'rb')

if __name__ == "__main__":
    main()