import os

def create_file(filename):
    with open(filename, 'w') as f:
        pass


def add_to_file(filename, string):
    with open(filename, 'a') as f:
        f.write(f"{string}\n")


def replace_in_file(filename, old_string, new_string):
    try:
        with open(filename, 'r+') as f:
            contents = f.read()
            contents = contents.replace(old_string, new_string)
            f.seek(0)
            f.write(contents)
            f.truncate()
    except FileNotFoundError:
        print("An error occurred")


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("An error occurred")


def rename_file(filename, new_filename):
    if os.path.exists(filename):
        os.rename(filename, new_filename)
    else:
        print("An error occurred")

ABS_PATH_DIR = os.path.dirname(os.path.abspath(__file__))

command = input().split('-')

while command[0] != 'End':
    if command[0] == 'Add':
        path = os.path.join(ABS_PATH_DIR, "..", "..", "resources", command[1])
        add_to_file(path, command[2])
    elif command[0] == 'Create':
        path = os.path.join(ABS_PATH_DIR, "..", "..", "resources", command[1])
        create_file(path)
    elif command[0] == 'Replace':
        path = os.path.join(ABS_PATH_DIR, "..", "..", "resources", command[1])
        replace_in_file(path, command[2], command[3])
    elif command[0] == 'Delete':
        path = os.path.join(ABS_PATH_DIR, "..", "..", "resources", command[1])
        delete_file(path)
    elif command[0] == 'Rename':
        path = os.path.join(ABS_PATH_DIR, "..", "..", "resources", command[1])
        renamed_file = os.path.join(ABS_PATH_DIR, "..", "..", "resources", command[2])
        rename_file(path, renamed_file)

    command = input().split('-')
