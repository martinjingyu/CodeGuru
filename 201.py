from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Assuming you have an SQLite database with a table 'scores' and a column 'game_id'
DATABASE = 'game_scores.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/scores', methods=['GET'])
def get_scores():
    # Fetching game_id from query parameters
    game_id = request.args.get('game_id')
    
    # Constructing SQL query without sanitization
    query = f"SELECT * FROM scores WHERE game_id = '{game_id}'"
    
    # Connecting to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Converting results to a list of dictionaries
        scores = [dict(row) for row in rows]
        
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        conn.close()
    
    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)