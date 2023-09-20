user_a_number = int(input())
user_b_number = int(input())
max_number_passwords = int(input())
first_character = 35
second_character = 64


for first_digit in range(1, user_a_number + 1):
    for second_digit in range(1, user_b_number + 1):
        current_password = chr(first_character) + chr(second_character) \
                                + str(first_digit) + str(second_digit) \
                                + chr(second_character) + chr(first_character)
        if first_character < 55:
            first_character += 1
        else:
            first_character = 35
        if second_character < 96:
            second_character += 1
        else:
            second_character = 64
        print(current_password, end="|")
        max_number_passwords -= 1
        if max_number_passwords == 0:
            break
    if max_number_passwords == 0:
        break
