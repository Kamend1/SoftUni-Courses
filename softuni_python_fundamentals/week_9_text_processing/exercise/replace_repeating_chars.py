string = input()
new_string = ""

for index in range(len(string) - 1):
    if string[index] != string[index + 1]:
        new_string += string[index]
new_string += string[-1]

print(new_string)
