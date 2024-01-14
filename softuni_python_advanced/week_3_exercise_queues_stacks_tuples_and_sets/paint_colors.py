from collections import deque

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ["orange", "purple", "green"]

substrings = deque(x for x in input().split())

colors_found = []

while substrings:
    if len(substrings) == 1:
        test_string = substrings[0]
        test_string_1 = ""
    else:
        test_string = substrings[0] + substrings[-1]
        test_string_1 = substrings[-1] + substrings[0]
    if test_string in main_colors or test_string in secondary_colors:
        colors_found.append(test_string)
        if len(substrings) >= 1:
            substrings.popleft()
        if len(substrings) >= 1:
            substrings.pop()
    elif test_string_1 in secondary_colors or test_string_1 in main_colors:
        colors_found.append(test_string_1)
        if len(substrings) >= 1:
            substrings.popleft()
        if len(substrings) >= 1:
            substrings.pop()
    else:
        new_string_1 = substrings[0][:-1]
        new_string_2 = substrings[-1][:-1]
        if len(substrings) >= 1:
            substrings.popleft()
        if len(substrings) >= 1:
            substrings.pop()
        if new_string_1:
            substrings.insert(len(substrings) // 2, new_string_1)
        if new_string_2:
            substrings.insert(len(substrings) // 2, new_string_2)

if "orange" in colors_found:
    if "red" not in colors_found  or "yellow" not in colors_found:
        for color in colors_found:
            if color == "orange":
                colors_found.remove(color)
elif "purple" in colors_found:
    if "red" not in colors_found  or "blue" not in colors_found:
        for color in colors_found:
            if color == "purple":
                colors_found.remove(color)
elif "green" in colors_found:
    if "yellow" not in colors_found  or "blue" not in colors_found:
        for color in colors_found:
            if color == "green":
                colors_found.remove(color)

print(colors_found)
