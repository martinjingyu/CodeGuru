import os

def delete_file():
    file_path = input("Please enter the path of the file you want to delete: ")
    os.remove(file_path)
    print(f"File '{file_path}' has been deleted.")

# Example usage:
# delete_file()