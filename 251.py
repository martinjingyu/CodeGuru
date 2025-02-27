from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/user-input', methods=['GET'])
def user_input():
    # Retrieve user input from query parameters
    user_input = request.args.get('input', '')
    
    # Construct a response message incorporating user input without sanitization
    response_message = f"User provided input: {user_input}"
    
    # Create a response object
    response = make_response(response_message)
    
    # Set the Content-Type header
    response.headers['Content-Type'] = 'text/html'
    
    return response

if __name__ == '__main__':
    app.run(debug=True)