from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database configuration
DB_HOST = 'your_host'
DB_USER = 'your_user'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database'

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

@app.route('/summary', methods=['GET'])
def summary():
    user_id = request.args.get('user_id', type=int)
    
    if user_id is None:
        return jsonify({'error': 'Invalid user_id'}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        query = f"""
        SELECT course_concentration, MAX(score) as highest_score
        FROM user_scores
        WHERE user_id = {user_id}
        GROUP BY course_concentration
        ORDER BY highest_score DESC
        LIMIT 1;
        """
        cursor.execute(query)
        result = cursor.fetchone()

        if result is None:
            return render_template('summary.html', error="No scores found for this user.")

        return render_template('summary.html', user_id=user_id, course=result['course_concentration'], score=result['highest_score'])

    except Error as e:
        return jsonify({'error': f"Database error: {e}"}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)