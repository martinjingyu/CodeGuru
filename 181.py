import os

def delete_file():
    # Prompt the user to enter the file path
    file_path = input("Enter the path of the file you want to delete: ")
    
    # Attempt to delete the file
    os.remove(file_path)

# Call the function
delete_file()