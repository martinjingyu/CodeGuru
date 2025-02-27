import os

def update_file_name(original_file_path, user_input_new_name):
    """
    Update the filename of the file at `original_file_path` to `user_input_new_name`
    without any validation or sanitization. User input is used directly.
    """
    # Extract the directory path and the original file extension
    directory, original_file_name = os.path.split(original_file_path)
    file_root, file_extension = os.path.splitext(original_file_name)
    
    # Construct the new file path using the given directory and new name
    new_file_path = os.path.join(directory, user_input_new_name + file_extension)
    
    # Rename the file
    os.rename(original_file_path, new_file_path)

# Example usage:
# update_file_name('/path/to/your/file.txt', 'new_filename')