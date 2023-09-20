first_number_n = int(input())
second_number_l = int(input())

for first_character in range(1, first_number_n + 1):
    for second_character in range(1, first_number_n + 1):
        for third_character in range(97, 97 + second_number_l):
            for fourth_character in range(97, 97 + second_number_l):
                if first_character >= second_character:
                    for fifth_character in range(first_character + 1, first_number_n + 1):
                        current_password = str(first_character) + str(second_character) \
                                        + chr(third_character) + chr(fourth_character) \
                                        + str(fifth_character)
                        print(current_password, end=" ")
                if second_character > first_character:
                    for fifth_character in range(second_character + 1, first_number_n + 1):
                        current_password = str(first_character) + str(second_character) \
                                        + chr(third_character) + chr(fourth_character) \
                                        + str(fifth_character)
                        print(current_password, end=" ")
