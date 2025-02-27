from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory 'database' for demonstration purposes
user_profiles = {
    '1': {'name': 'Alice', 'email': 'alice@example.com'},
    '2': {'name': 'Bob', 'email': 'bob@example.com'}
}

@app.route('/profile/<user_id>', methods=['GET', 'POST'])
def profile(user_id):
    if request.method == 'GET':
        # Retrieve user profile
        profile = user_profiles.get(user_id, None)
        if profile:
            return jsonify(profile)
        else:
            return jsonify({'error': 'User not found'}), 404

    elif request.method == 'POST':
        # Update user profile
        data = request.json
        if user_id in user_profiles:
            # Directly update the profile without any validation or sanitization
            user_profiles[user_id].update(data)
            return jsonify({'message': 'Profile updated successfully'})
        else:
            # Create a new profile if it doesn't exist
            user_profiles[user_id] = data
            return jsonify({'message': 'Profile created successfully'})

if __name__ == '__main__':
    app.run(debug=True)