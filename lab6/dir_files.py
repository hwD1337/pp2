#Python program to list only directories, files and all directories, files in a specified path:
import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)

path = "(your path)"
print("Directories:", list_directories(path))
print("Files:", list_files(path))
print("All directories and files:", list_all(path))

#Python program to check for access to a specified path (existence, readability, writability, executability):
import os

def check_access(path):
    return {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }

path = "(your path)"
access_info = check_access(path)
print("Access information:", access_info)

#Python program to test whether a given path exists or not, and find the filename and directory portion if it does:
import os

def check_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    return False, None, None

path = "(your path)"
exists, filename, directory = check_path(path)
print(f"Path exists: {exists}")
if exists:
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")

#Python program to count the number of lines in a text file:
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())

file_path = "file.txt"
line_count = count_lines(file_path)
print("Number of lines in the file:", line_count)

#Python program to write a list to a file:
def write_list_to_file(lst, file_path):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

lst = ["item1", "item2", "item3"]
file_path = "output.txt"
write_list_to_file(lst, file_path)
print("List written to file")

#Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt:
import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt")

generate_files()
print("26 text files generated")

#Python program to copy the contents of a file to another file:
def copy_file(source, destination):
    with open(source, 'r') as src:
        content = src.read()
    with open(destination, 'w') as dst:
        dst.write(content)

source_path = "source.txt"
destination_path = "destination.txt"
copy_file(source_path, destination_path)
print("Contents copied to another file")

#Python program to delete file by specified path (check for access and existence):
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            return f"File '{path}' has been deleted"
        else:
            return f"Access denied: Cannot delete '{path}'"
    else:
        return f"File '{path}' does not exist"

path = "file_to_delete.txt"
result = delete_file(path)
print(result)
