import os

def generate_massive_text(size=1024):
    """Generates a large string of text."""
    text = "A" * size  # Generate a string of 'A's of specified size
    return text

def write_to_file(file_name, text):
    """Writes the provided text to a file."""
    with open(file_name, 'w') as file:
        file.write(text)

def create_files_infinite():
    """Writes massive text to new files in an infinite loop."""
    iteration = 0
    while True:
        # Generate a file name with the current iteration number
        file_name = f"massive_text_file_{iteration}.txt"
        
        # Generate massive text
        text = generate_massive_text(size=10**6)  # 1 MB of text
        
        # Write the text to the file
        write_to_file(file_name, text)
        
        # Output status
        print(f"File '{file_name}' created with size {len(text)} bytes.")
        
        iteration += 1

if __name__ == "__main__":
    try:
        create_files_infinite()
    except KeyboardInterrupt:
        print("Process interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(f"An error occurred: {e}")