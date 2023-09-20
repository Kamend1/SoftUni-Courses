user_number = int(input())
sum_first_two_digits = 0
sum_last_two_digits = 0

for number in range(1111, 9999 + 1):
    current_number = str(number)
    current_number_is_lucky = True
    for current_digit in current_number:
        if int(current_digit) == 0:
            current_number_is_lucky = False
            break
    sum_first_two_digits = int(current_number[0]) + int(current_number[1])
    sum_last_two_digits = int(current_number[2]) + int(current_number[3])
    if current_number_is_lucky and sum_first_two_digits == sum_last_two_digits and user_number % sum_first_two_digits == 0:
        print(number, end=" ")
