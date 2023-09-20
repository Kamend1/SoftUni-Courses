single_digit_beginning = int(input())
single_digit_end = int(input())
number_is_special = False

for first_digit in range(single_digit_beginning, single_digit_end + 1):
    for second_digit in range(single_digit_beginning, single_digit_end + 1):
        for third_digit in range(single_digit_beginning, single_digit_end + 1):
            for fourth_digit in range(single_digit_beginning, single_digit_end + 1):
                current_number_str = str(first_digit) + str(second_digit) \
                                     + str(third_digit) + str(fourth_digit)
                if ((int(first_digit) % 2 == 0 and int(fourth_digit) % 2 != 0) \
                        or (int(first_digit) % 2 != 0 and int(fourth_digit) % 2 == 0)) \
                        and int(first_digit) > int(fourth_digit) \
                        and (int(second_digit) + int(third_digit)) % 2 == 0:
                    print(current_number_str, end=" ")
