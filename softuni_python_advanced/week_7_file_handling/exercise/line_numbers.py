import os.path
from string import punctuation

ABSOLUTE_PATH_DIR = os.path.dirname(os.path.abspath(__file__))
file_to_read = 'input.txt'
path_to_read = os.path.join(ABSOLUTE_PATH_DIR, "..", "..", "resources", file_to_read)

with open(path_to_read) as fr_file:
    lines = fr_file.readlines()

file_to_write = 'output_line_numbers.txt'
path_to_write = os.path.join(ABSOLUTE_PATH_DIR, "..", "..", "resources", file_to_write)
line_counter = 0

for line in lines:
    punctuation_counter = 0
    letter_counter = 0
    line_counter += 1
    for char in line:
        if char in punctuation:
            punctuation_counter += 1
        elif char.isalpha():
            letter_counter += 1
    new_line = f"Line {line_counter}: {line.strip()} ({letter_counter})({punctuation_counter})\n"
    with open(path_to_write, "a") as fw_file:
        fw_file.write(new_line)
