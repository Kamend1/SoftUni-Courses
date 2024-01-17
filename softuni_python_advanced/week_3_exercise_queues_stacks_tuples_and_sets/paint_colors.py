from collections import deque

colors = ['red', 'yellow', 'blue', "orange", "purple", "green"]

req_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'},
}

substrings = deque(x for x in input().split())

colors_found = []

while substrings:
    test_string_1 = substrings.popleft()
    test_string_2 = substrings.pop() if substrings else ''
    combined_test_string = test_string_1 + test_string_2
    reverse_test_string = test_string_2 + test_string_1

    if combined_test_string in colors:
        colors_found.append(combined_test_string)
    elif reverse_test_string in colors:
        colors_found.append(reverse_test_string)
    else:
        new_string_1 = test_string_1[:-1]
        new_string_2 = test_string_2[:-1]

        if new_string_1:
            substrings.insert(len(substrings) // 2, new_string_1)
        if new_string_2:
            substrings.insert(len(substrings) // 2, new_string_2)

for color in set(req_colors.keys()).intersection(colors_found):
    if not req_colors.get(color).issubset(colors_found):
        colors_found.remove(color)

print(colors_found)
