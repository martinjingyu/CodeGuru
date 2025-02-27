from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/latest-article', methods=['GET'])
def latest_article():
    # Get user input from query parameter
    category = request.args.get('category')

    # WARNING: Do not use this approach in production!
    # This is a demonstration of insecure code.
    query = f"SELECT title FROM articles WHERE category = '{category}' ORDER BY published_date DESC LIMIT 1;"

    # Connect to the database and execute the query
    connection = sqlite3.connect('articles.db')
    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    if result:
        return jsonify({'title': result[0]})
    else:
        return jsonify({'error': 'No articles found for the given category'}), 404

if __name__ == '__main__':
    app.run(debug=True)