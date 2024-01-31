import os.path

ABSOLUTE_PATH_DIR = os.path.dirname(os.path.abspath(__file__))
file_to_read = 'input.txt'
path_to_read = os.path.join(ABSOLUTE_PATH_DIR, "..", "..", "resources", file_to_read)

with open(path_to_read) as fr_file:
    lines = fr_file.readlines()

file_to_write = 'output_even_lines.txt'
path_to_write = os.path.join(ABSOLUTE_PATH_DIR, "..", "..", "resources", file_to_write)
characters_set = {"-", ",", ".", "!", "?"}


with open(path_to_write, "w") as fw_file:
    for idx in range(len(lines)):
        if idx % 2 == 0:
            string_to_add = ''
            new_line = lines[idx].split()

            for el in reversed(new_line):
                print(el)
                for char in el:
                    if char in characters_set:
                        el = el.replace(char, '@')
                string_to_add += el + " "


        fw_file.write(f"{string_to_add}\n")