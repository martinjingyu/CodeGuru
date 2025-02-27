from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def fetch_user_profile(username):
    # WARNING: This is insecure code and should not be used in real applications.
    
    # Connect to your database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Insecure way: directly incorporating the username into the SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        user_profile = cursor.fetchone()
    except Exception as e:
        return {"error": str(e)}

    finally:
        conn.close()

    if user_profile:
        # Assuming the user_profile contains (id, username, email, etc.)
        return {
            "id": user_profile[0],
            "username": user_profile[1],
            "email": user_profile[2],
            # Add other fields as appropriate
        }
    else:
        return {"error": "User not found"}

@app.route('/profile', methods=['GET'])
def profile():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user_profile = fetch_user_profile(username)
    return jsonify(user_profile)

if __name__ == '__main__':
    app.run(debug=True)