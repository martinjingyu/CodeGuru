from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Define the directory where video files are stored
VIDEO_DIRECTORY = '/path/to/video/files'

@app.route('/delete_video', methods=['POST'])
def delete_video():
    try:
        # Get the filename from the user input
        filename = request.form.get('filename')

        # Path to the file
        file_path = os.path.join(VIDEO_DIRECTORY, filename)

        # Delete the file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)
            return jsonify(success=True, message='File deleted successfully.')
        
        return jsonify(success=False, message='File not found.')

    except Exception as e:
        return jsonify(success=False, message=f'An error occurred: {str(e)}'), 500

if __name__ == '__main__':
    app.run(debug=True)