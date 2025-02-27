from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form method="post" action="/submit">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <label for="age">Age:</label>
        <input type="text" id="age" name="age">
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    
    # Insecure way to create SQL query directly with user input
    query = f"INSERT INTO users (name, age) VALUES ('{name}', '{age}')"
    
    # Connect to the database and execute the unsafe query
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        result_message = f"User {name} added successfully."
    except sqlite3.Error as e:
        result_message = f"Database error: {e}"
    finally:
        conn.close()
    
    return render_template_string('<p>{{ result_message }}</p>', result_message=result_message)

if __name__ == '__main__':
    # Create table if it doesn't exist
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
    app.run(debug=True)