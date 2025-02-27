from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Simple HTML template to display the result
html_template = """
<!doctype html>
<html>
    <head><title>Book Title Lookup</title></head>
    <body>
        <h1>Book Title Lookup</h1>
        <form method="GET">
            <input type="text" name="title" placeholder="Enter book title">
            <input type="submit" value="Search">
        </form>
        {% if book_title %}
            <h2>Book Title: {{ book_title }}</h2>
        {% endif %}
    </body>
</html>
"""

@app.route('/')
def search_book():
    # Get the user input from the query string
    title_input = request.args.get('title', '')

    # Connect to the SQLite database
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Construct SQL query with user input directly (DO NOT DO THIS IN PRODUCTION!)
    query = f"SELECT title FROM books WHERE title LIKE '%{title_input}%'"

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        book_title = result[0] if result else "No book found."
    except Exception as e:
        book_title = f"An error occurred: {str(e)}"
    finally:
        conn.close()

    # Render the result using the HTML template
    return render_template_string(html_template, book_title=book_title)

if __name__ == '__main__':
    app.run(debug=True)