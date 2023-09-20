upper_bound_first_digit = int(input())
upper_bound_middle_digit = int(input())
upper_bound_third_digit = int(input())

for first_digit in range(2, upper_bound_first_digit + 1, 2):
    for middle_digit in range(2, upper_bound_middle_digit + 1):
        middle_digit_is_prime = True
        if middle_digit != 2:
            for i in range(2, middle_digit):
                if middle_digit % i == 0:
                    middle_digit_is_prime = False
                    break
        if middle_digit_is_prime:
            for last_digit in range(2, upper_bound_third_digit + 1, 2):

                print(f"{first_digit} {middle_digit} {last_digit}")
