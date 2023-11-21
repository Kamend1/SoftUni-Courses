import re

command_input = input()
pattern = r"(w{3}\.[a-zA-Z0-9\.\-]+\.[a-z]+)"

while command_input:
    match = re.search(pattern, command_input)
    if match:
        print(match.group(1))
    command_input = input()
