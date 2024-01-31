import os

ABSOLUTE_PATH_DIR = os.path.dirname(os.path.abspath(__file__))
filename = "numbers.txt"

path = os.path.join(ABSOLUTE_PATH_DIR, "..", "resources", filename)

file = open(path, "r")
lines = file.readlines()

sum_numbers = 0

for line in lines:
    sum_numbers += int(line.strip())

file.close()

print(sum_numbers)