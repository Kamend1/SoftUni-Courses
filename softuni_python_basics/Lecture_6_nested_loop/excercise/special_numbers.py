number = int(input())

for current_number in range(1111, 9999 + 1):
    current_number_str = str(current_number)
    current_is_special = True
    for current_digit in current_number_str:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            current_is_special = False
            break
    if current_is_special:
        print(current_number, end=" ")
