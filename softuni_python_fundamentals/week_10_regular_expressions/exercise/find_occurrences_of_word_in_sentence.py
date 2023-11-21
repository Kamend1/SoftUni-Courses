import re

text = input()
search_pattern = input()

pattern = f"\\b{search_pattern}\\b"

matches = re.findall(pattern, text, flags=re.IGNORECASE)

print(len(matches))
