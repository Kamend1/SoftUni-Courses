def decipher_message(message: list):
    for idx in range(len(message)):
        word = message[idx]
        new_word = ""
        if word[0:3].isdigit():
            order = int(word[0:3])
            character = chr(order)
            new_word = character + word[3:]
        elif word[0:2].isdigit():
            order = int(word[0:2])
            character = chr(order)
            new_word = character + word[2:]
        message[idx] = new_word


    for j in range(len(message)):
        chr_list = []
        element = message[j]
        for character in element:
            chr_list.append(character)
        chr_list[1], chr_list[-1] = chr_list[-1], chr_list[1]
        element = "".join(chr_list)
        message[j] = element


    return message

ciphered_message = input().split()
result = decipher_message(ciphered_message)
print(*result, sep=" ")
