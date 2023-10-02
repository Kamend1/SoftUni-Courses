def characters_in_range(char_1, char_2):
    new_string = ""
    for ord_char in range(ord(char_1) + 1, ord(char_2)):
        new_string += chr(ord_char) + " "
    return new_string.rstrip()

char_1 = input()
char_2 = input()
print(characters_in_range(char_1, char_2))
