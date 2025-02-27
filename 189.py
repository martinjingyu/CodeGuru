from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_post_title', methods=['GET'])
def get_post_title():
    post_id = request.args.get('id')
    
    # WARNING: This is an insecure method and vulnerable to SQL injection.
    query = f"SELECT title FROM posts WHERE id = '{post_id}'"
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        
        if row:
            return jsonify({"title": row['title']})
        else:
            return jsonify({"error": "Post not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)