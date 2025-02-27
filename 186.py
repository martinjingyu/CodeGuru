from flask import Flask, request, jsonify
import yaml
import os

app = Flask(__name__)

def process_user_input(user_input):
    """
    Takes a string of user input, converts it to YAML format, and saves it to a configuration file.
    
    :param user_input: str - The user input string to process and save as YAML.
    """
    # Define the configuration file path
    config_file_path = 'config.yaml'
    
    # Convert the string to a dictionary by assuming it's in YAML format
    try:
        data = yaml.safe_load(user_input)
        
        # Ensure data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("Processing error: Converted data is not a dictionary.")
        
        # Save the data to a YAML file
        with open(config_file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
            
        return f"Data successfully processed and saved to {config_file_path}"
    
    except yaml.YAMLError as e:
        return f"Error processing YAML: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/process', methods=['POST'])
def handle_post_request():
    """
    Flask route to handle HTTP POST requests containing user input.
    """
    user_input = request.get_data(as_text=True)
    if not user_input:
        return jsonify({'error': 'No input received'}), 400
    
    result = process_user_input(user_input)
    return jsonify({'message': result})

if __name__ == '__main__':
    # Ensure the config.yaml file exists
    if not os.path.exists('config.yaml'):
        open('config.yaml', 'a').close()

    app.run(debug=True)