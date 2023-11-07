filepath_string = input()
len_filepath = len(filepath_string)
file_extension = ""
file_name = ""
index = 0

while True:
    task_ext_complete = False
    for idx in range(len_filepath - 1, 0, -1):
        if filepath_string[idx] == ".":
            task_ext_complete = True
            index = idx
            break
        else:
            file_extension += filepath_string[idx]
    if task_ext_complete:
        break

while True:
    task_name_complete = False
    for idx in range(index - 1, 0, -1):
        if filepath_string[idx] == "\\":
            task_name_complete = True
            break
        else:
            file_name += filepath_string[idx]
    if task_name_complete:
        break

file_name = file_name[::-1]
file_extension = file_extension[::-1]

print(f"File name: {file_name}\nFile extension: {file_extension}")
