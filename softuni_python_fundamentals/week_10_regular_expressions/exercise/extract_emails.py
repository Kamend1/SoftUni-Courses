import re

pattern = r"^|(?<=\s)(\b([A-Za-z0-9][A-Za-z0-9\.\-\_]+)@([A-Za-z]+[\-]?[A-Za-z]+)\.([\.a-z]+)*\b)"
text = input()

matches = re.findall(pattern, text, flags=re.IGNORECASE)

for match in matches:
    print(match[0])
