import re

text = input()
regex = r"(\d{2})(\S)([A-Z][a-z]{2})\2([0-9]{4})"

matches = re.findall(regex, text)

for date in matches:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
