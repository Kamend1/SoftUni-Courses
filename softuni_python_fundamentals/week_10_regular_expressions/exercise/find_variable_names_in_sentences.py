import re

pattern = r"\b_[a-zA-Z0-9]+\b"

text = input()

matches = re.findall(pattern, text)

print(",".join(match[1:] for match in matches))
