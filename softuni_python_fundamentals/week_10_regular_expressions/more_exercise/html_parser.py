import re

text = input()

title_pattern = r"\<title\>(?P<title>.+)\<\/?title\>"
body_pattern = "<body>.+</body>"
sub_pattern = r"<[^>]+>"
sub_pattern_1 = r"\\n"

title = re.findall(title_pattern, text)[0]
body = re.findall(body_pattern, text)[0]
first_step_clean_body = re.sub(sub_pattern, "", body)
final_clean_body = re.sub(sub_pattern_1, "", first_step_clean_body)

print(f"Title: {title}")
print(f"Content: {final_clean_body}")
