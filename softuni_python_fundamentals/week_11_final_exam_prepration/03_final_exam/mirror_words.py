import re

string = input()
pattern = (r"(#(?P<word_1>[a-zA-Z]{3,})##(?P<word_2>[a-zA-Z]{3,})#)"
           r"|(@(?P<word_3>[a-zA-Z]{3,})@@(?P<word_4>[a-zA-Z]{3,})@)")
mirror_words = []

matches = re.findall(pattern, string)

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

for match in matches:
    if match[0]:
        if match[1] == match[2][::-1]:
            mirror_words.append((match[1], match[2]))
    else:
        if match[4] == match[5][::-1]:
            mirror_words.append((match[4], match[5]))

if mirror_words:
    print("The mirror words are:")
    print(", ".join(f"{pair[0]} <=> {pair[1]}" for pair in mirror_words))
else:
    print("No mirror words!")
