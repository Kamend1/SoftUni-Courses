string = input()

capital_list = []
idx = 0

for character in string:
    if 65 <= ord(character) <= 90:
        capital_list.append(idx)

    idx += 1

print(capital_list)
