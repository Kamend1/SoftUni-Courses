import os.path

ABSOLUTE_PATH_FILE = os.path.dirname(os.path.abspath(__file__))
filename = 'text.txt'

path = os.path.join(ABSOLUTE_PATH_FILE, "..", "resources", filename)

try:
    file = open(path)
    print("File found")
except FileNotFoundError:
    print("File not found")
