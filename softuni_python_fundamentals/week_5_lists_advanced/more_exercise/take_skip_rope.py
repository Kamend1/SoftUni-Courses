string = input()
numbers_list = []
characters_list = []
takes_list = []
skips_list = []
hidden_string = []

for char in string:
    if char.isdigit():
        numbers_list.append(int(char))
    else:
        characters_list.append(char)

for idx in range(len(numbers_list)):
    if idx % 2 == 0:
        takes_list.append(numbers_list[idx])
    else:
        skips_list.append(numbers_list[idx])

idx_takes = 0
idx_skips = 0

for turns in range(2*len(skips_list)):
    if turns % 2 == 0:
        num_char_taken = takes_list[idx_takes]
        hidden_string += characters_list[:num_char_taken]
        characters_list = characters_list[num_char_taken:]
        idx_takes += 1
    else:
        num_char_removed = skips_list[idx_skips]
        characters_list = characters_list[num_char_removed:]
        idx_skips += 1


print(*hidden_string, sep="")
