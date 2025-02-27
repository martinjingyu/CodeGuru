from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Define the directory where your videos are stored
VIDEO_DIR = '/path/to/your/video/directory'

@app.route('/delete_video', methods=['POST'])
def delete_video():
    # Get the filename from the JSON payload
    data = request.get_json()
    filename = data.get('filename')
    
    if not filename:
        return jsonify({'error': 'Filename is required'}), 400

    # Construct the full file path
    file_path = os.path.join(VIDEO_DIR, filename)

    # Attempt to delete the file
    try:
        os.remove(file_path)
        return jsonify({'message': f'{filename} has been deleted successfully'}), 200
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)