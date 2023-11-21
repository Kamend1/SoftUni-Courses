import re

text = input()
pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"

matches = re.findall(pattern, text)

print(' '.join(matches))
