import os.path
import re

ABSOLUTE_PATH_DIR = os.path.dirname(os.path.abspath(__file__))
file_to_search = 'words.txt'
path_search = os.path.join(ABSOLUTE_PATH_DIR,"..", "resources", file_to_search)
words_to_search = []
counted_words = {}

with open(path_search, "r") as fs_file:
    for line in fs_file.readlines():
        words_to_search = [word for word in line.split()]
        for word in words_to_search:
            counted_words[word] = 0


file_to_read = 'input.txt'
path_read = os.path.join(ABSOLUTE_PATH_DIR, "..", "resources", file_to_read)

with open(path_read, "r") as fs_read:
    lines = fs_read.readlines()

    for word in words_to_search:
        pattern = re.compile(rf"\b{word}\b")

        for line in lines:
            line = line.lower()
            matches = re.findall(pattern, line)
            counted_words[word] += len(matches)

    counted_words = dict(sorted(counted_words.items(), key=lambda x: -x[1]))

file_to_write = 'output.txt'
path_to_write = os.path.join(ABSOLUTE_PATH_DIR, "..", "resources", file_to_write)

with open(path_to_write, 'w') as fw_file:
    for k, v in counted_words.items():
        fw_file.write(f"{k} - {v}\n")
