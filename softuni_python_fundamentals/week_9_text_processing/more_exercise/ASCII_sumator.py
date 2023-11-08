start_char = input()
end_char = input()

start_ascii = ord(start_char)
end_ascii = ord(end_char)

string_to_search = input()
sum_ascii = 0

for char in string_to_search:
    if start_ascii < ord(char) < end_ascii:
        sum_ascii += ord(char)

print(sum_ascii)
