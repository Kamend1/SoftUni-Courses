import re

pattern = r"[0-9]+"
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        print(match, end=" ")
