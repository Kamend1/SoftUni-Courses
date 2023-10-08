string_list = input().split(", ")
strings_to_check = input().split(", ")
contained_strings = []

for string1 in string_list:
    for string2 in strings_to_check:
        if string1 in string2:
            if string1 not in contained_strings:
                contained_strings.append(string1)

print(contained_strings)
