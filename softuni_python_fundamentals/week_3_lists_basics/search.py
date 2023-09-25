n = int(input())
search_string = input()
all_strings = []
match_strings = []

for string in range(n):
    string = input()
    all_strings.append(string)
    if search_string in string:
        match_strings.append(string)

print(all_strings)
print(match_strings)
