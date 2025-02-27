from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'GET':
        # Unsafe example for educational purposes
        new_name = request.args.get('name')
        new_email = request.args.get('email')
        if new_name and new_email:
            sql = f"UPDATE users SET name = '{new_name}', email = '{new_email}' WHERE id = {user_id}"
            # Execute the unsafe SQL query
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return jsonify({'message': 'User updated successfully'})
    
    elif request.method == 'POST':
        data = request.get_json()
        new_name = data.get('name')
        new_email = data.get('email')
        if new_name and new_email:
            sql = f"UPDATE users SET name = '{new_name}', email = '{new_email}' WHERE id = {user_id}"
            # Execute the unsafe SQL query
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return jsonify({'message': 'User updated successfully'})

    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True)