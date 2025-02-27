from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

def create_users_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def generate_token(username, hashed_password):
    # Simple token generation using SHA-256
    token_source = f"{username}:{hashed_password}".encode()
    token = hashlib.sha256(token_source).hexdigest()
    return token

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # WARNING: This query directly interpolates user input, demonstrating SQL injection risk
    query = f"SELECT username, password FROM users WHERE email = '{email}'"
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        username, stored_password = user
        # Hash the provided password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Compare hashed passwords
        if hashed_password == stored_password:
            token = generate_token(username, hashed_password)
            return jsonify({'token': token}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    create_users_table()
    app.run(debug=True)