string = input()
new_string = ""
strength = 0

for index in range(len(string)):
    if string[index] != ">" and strength == 0:
        new_string += string[index]
    elif string[index] != ">" and strength != 0:
        strength -= 1
    elif string[index] == ">":
        new_string += string[index]
        strength += int(string[index + 1])

print(new_string)
