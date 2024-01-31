import os.path

ABSOLUTE_PATH_DIR = os.path.dirname(os.path.abspath(__file__))


file_name = 'my_first_file.txt'
path = os.path.join(ABSOLUTE_PATH_DIR, "..", "resources", file_name)

with open(path, 'a') as f:
    f.write("I just created my first file!")
