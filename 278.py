import sqlite3

def get_top_n_users_by_karma(n):
    # Establish a connection to the database
    conn = sqlite3.connect('irc_chat.db')
    cursor = conn.cursor()

    # WARNING: This is an insecure way to construct an SQL query!
    # Never do this in production code.
    query = f"SELECT username, karma FROM users ORDER BY karma DESC LIMIT {n};"

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print("Top users by karma:")
        for user in results:
            print(f"Username: {user[0]}, Karma: {user[1]}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Example usage:
# get_top_n_users_by_karma(5)