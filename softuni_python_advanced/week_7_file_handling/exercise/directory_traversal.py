import os

ABS_PATH_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(ABS_PATH_DIR,"..", "..", "resources", "example_resources")
files_by_extension = {}

report_path = os.path.join(path, "report.txt")
if os.path.exists(report_path):
    os.remove(report_path)

for file in os.listdir(path):
    filename, extension = os.path.splitext(file)
    if extension not in files_by_extension:
        files_by_extension[extension] = []
    files_by_extension[extension].append(file)

for k, v in files_by_extension.items():
    with open(report_path, 'a') as f:
        f.write(f"{k}\n")
    for file in v:
        with open(report_path, 'a') as f:
            f.write(f"- - - {file}\n")
