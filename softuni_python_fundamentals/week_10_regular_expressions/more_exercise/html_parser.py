import re

text = input()

title_pattern = r"<title>(\w+)<\/title>"
body_pattern = ""

title = re.search(title_pattern, text)
body = re.search(body_pattern, text)

print(f"Title: {title}")
print(f"Content: {body}")
