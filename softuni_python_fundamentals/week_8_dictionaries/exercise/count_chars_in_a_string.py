string = input()
string_dict = {}

for char in string:
    if char == " ":
        continue
    else:
        if char not in string_dict.keys():
            string_dict[char] = 1
        else:
            string_dict[char] += 1

for char, count in string_dict.items():
    print(f"{char} -> {count}")
