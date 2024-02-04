import os


def traverse_dir(directory, file_searched, file_new_name, first_level=False, ):
    for filename in os.listdir(directory):
        # Construct the full path to the file
        file_path = os.path.join(directory, filename)
        if filename == file_searched:
            new_file_path = os.path.join(directory, file_new_name)
            rename_file(file_path, new_file_path)
            return True

        elif os.path.isdir(file_path) and not first_level:  # Check if it's a directory
            traverse_dir(file_path, file_searched, file_new_name, first_level=True)
    else:
        return False

def rename_file(filename, new_filename):
    if os.path.exists(filename):
        os.rename(filename, new_filename)
    else:
        print("An error occurred")


ABS_PATH_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(ABS_PATH_DIR, "..", "..", "resources", "example_resources")
files_by_extension = {}
file_to_be_renamed = input("Input file name of existing file: ")
new_name = input("Input required new name: ")

print(traverse_dir(path, file_to_be_renamed, new_name, first_level=True))
