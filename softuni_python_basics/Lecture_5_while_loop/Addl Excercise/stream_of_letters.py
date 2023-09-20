user_letter = input()
counter_c = 0
counter_o = 0
counter_n = 0
secret_counter = 0
current_word_string = ''
printed_string = ''

while user_letter != "End":
    if 65 <= ord(user_letter) <= 90 or 97 <= ord(user_letter) <= 122:
        if ord(user_letter) == 99:
            if counter_c == 0:
                counter_c += 1
                secret_counter += 1
            else:
                current_word_string += user_letter
        elif ord(user_letter) == 110:
            if counter_n == 0:
                counter_n += 1
                secret_counter += 1
            else:
                current_word_string += user_letter
        elif ord(user_letter) == 111:
            if counter_o == 0:
                counter_o += 1
                secret_counter += 1
            else:
                current_word_string += user_letter
        else:
            current_word_string += user_letter
    if secret_counter == 3:
        current_word_string += chr(32)
        secret_counter = 0
        counter_c = 0
        counter_n = 0
        counter_o = 0
        printed_string += current_word_string
        current_word_string = ''
    user_letter = input()

print(printed_string)
