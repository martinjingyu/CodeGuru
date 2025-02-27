import sqlite3

def fetch_total_games_unsafe(player_id, season, db_path='games_database.db'):
    """
    Fetch the total number of games played by a specified player in a given season
    from a database, directly incorporating the player ID and season into the SQL query
    without any sanitization.

    :param player_id: The ID of the player.
    :param season: The season for which to fetch the total number of games.
    :param db_path: Path to the SQLite database file.
    :return: The total number of games played by the player in the specified season.
    """
    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # WARNING: This SQL injection-prone query should never be used in production code.
    query = f"SELECT COUNT(*) FROM games WHERE player_id = {player_id} AND season = '{season}'"
    
    # Execute the SQL query
    cursor.execute(query)
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    # Return the total number of games
    return result[0] if result else 0

# Example usage:
# total_games = fetch_total_games_unsafe(123, '2022-2023')
# print(total_games)