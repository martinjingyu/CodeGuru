import os

def delete_file_unsecured():
    """Delete a file specified by unvalidated user input."""
    # Directly take user input and pass it to os.remove(), which is insecure.
    file_to_delete = input("Enter the filename to delete: ")
    try:
        os.remove(file_to_delete)
        print(f"File '{file_to_delete}' has been deleted.")
    except FileNotFoundError:
        print(f"Error: The file '{file_to_delete}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to delete the file '{file_to_delete}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Note: This function is for demonstration only and should not be used in production code.