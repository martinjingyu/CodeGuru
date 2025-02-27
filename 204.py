from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/update_page', methods=['POST'])
def update_page():
    # Extract page name and content from the request
    data = request.json
    page_name = data['page_name']
    content = data['content']
    
    # Construct SQL query with direct string formatting
    # This is insecure and vulnerable to SQL injection
    sql = f"UPDATE pages SET content = '{content}' WHERE page_name = '{page_name}'"
    
    # Connect to the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    try:
        # Execute the query
        cursor.execute(sql)
        conn.commit()
        return jsonify({'success': True}), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)