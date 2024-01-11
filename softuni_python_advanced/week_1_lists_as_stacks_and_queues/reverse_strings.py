string = input()
string_stack = []

for char in string:
    string_stack.append(char)

new_string = ""
while string_stack:
    new_string += string_stack.pop()

print(new_string)
