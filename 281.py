from flask import Flask, render_template_string, request
import sqlite3

app = Flask(__name__)

@app.route('/profile/<username>')
def show_profile(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Unsafe SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    profile = cursor.fetchone()
    
    conn.close()
    
    if profile:
        return render_template_string("Username: {{ profile[0] }}<br>Email: {{ profile[1] }}", profile=profile)
    else:
        return "Profile not found."

if __name__ == '__main__':
    app.run(debug=True)