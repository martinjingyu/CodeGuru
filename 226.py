from flask import Flask, render_template_string, g
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Set up the database connection
DATABASE_URI = 'sqlite:///your_database.db'  # Update with your database URI
engine = create_engine(DATABASE_URI)

def get_db_connection():
    if 'db' not in g:
        g.db = engine.connect()
    return g.db

@app.teardown_appcontext
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/profile/<username>')
def profile(username):
    db = get_db_connection()
    # Unsafe query: direct use of user input
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = db.execute(text(query)).fetchone()

    if result is None:
        return "User not found", 404

    # Render a simple profile page (unsafe in terms of SQL, but acceptable for template rendering)
    return render_template_string('''
        <h1>User Profile</h1>
        <p>Username: {{ username }}</p>
        <p>Email: {{ email }}</p>
        <p>Name: {{ name }}</p>
    ''', username=result['username'], email=result['email'], name=result['name'])

if __name__ == '__main__':
    app.run(debug=True)