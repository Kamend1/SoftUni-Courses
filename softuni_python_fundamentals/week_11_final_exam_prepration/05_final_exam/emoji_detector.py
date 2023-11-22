import re

string = input()
digit_pattern = r"\d"
emoji_pattern = r"\*\*[A-Z][a-z]{2,}\*\*|::[A-Z][a-z]{2,}::"

digits = re.findall(digit_pattern, string)
emojis = re.findall(emoji_pattern, string)
cool_threshold = 1
cool_emojis = []

for digit in digits:
        cool_threshold *= int(digit)

if emojis:
    for emoji in emojis:
        current_cool_score = 0
        for char in emoji:
            if char != ":" and char != "*":
                current_cool_score += ord(char)
        if current_cool_score > cool_threshold:
            cool_emojis.append(emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(f"{emoji}")
