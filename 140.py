import zipfile
import os

def compress_files(file_paths, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in file_paths:
            if os.path.isfile(file):
                zipf.write(file, os.path.basename(file))
            else:
                print(f"Warning: {file} is not a file and was skipped.")

# Example usage
files_to_compress = ['file1.txt', 'file2.txt']
compress_files(files_to_compress, 'output.zip')