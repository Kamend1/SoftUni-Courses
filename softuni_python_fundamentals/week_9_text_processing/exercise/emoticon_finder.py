string = input()
emoticon_list = []

for index in range(len(string)):
    if string[index] == ":":
        emoticon_list.append((string[index] + string[index + 1]))

for emoticon in emoticon_list:
    print(emoticon)
