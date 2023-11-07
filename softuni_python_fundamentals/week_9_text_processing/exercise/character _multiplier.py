from sys import maxsize
strings = input().split()
result = 0
min_len = maxsize
string_min_len = 0

for index in range(len(strings)):
    if len(strings[index]) < min_len:
        min_len = len(strings[index])
        string_min_len = index

for idx in range(min_len):
    result += ord(strings[0][idx]) * ord(strings[1][idx])

if string_min_len == 0:
    for idx in range(len(strings[1]) - 1, min_len - 1, -1):
        result += ord(strings[1][idx])
elif string_min_len == 1:
    for idx in range(len(strings[0]) - 1, min_len - 1, -1):
        result += ord(strings[0][idx])

print(result)
