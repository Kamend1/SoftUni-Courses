import os


def traverse_dir(directory, first_level=False):
    for filename in os.listdir(directory):
        # Construct the full path to the file
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            current_file, extension = os.path.splitext(filename)
            if extension:
                files_by_extension[extension] = files_by_extension.get(extension, []) + [current_file]
        elif os.path.isdir(file_path) and not first_level:  # Check if it's a directory
            traverse_dir(file_path, first_level=True)


ABS_PATH_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(ABS_PATH_DIR, "..", "..", "resources", "example_resources")
files_by_extension = {}

report_path = os.path.join(path, "report.txt")
if os.path.exists(report_path):
    os.remove(report_path)

try:
    traverse_dir(path)
except FileNotFoundError:
    print("Directory does not exist")

files_by_extension = dict(sorted(files_by_extension.items(), key=lambda x: x[0]))
result = []

for k, v in files_by_extension.items():
    result.append(f"{k}\n")
    for file in sorted(v):
        result.append(f"- - - {file}\n")

with open(report_path, 'w') as f:
    for element in result:
        f.write(element)
