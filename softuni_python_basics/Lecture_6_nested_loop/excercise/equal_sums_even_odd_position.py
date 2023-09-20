number_first = int(input())
number_second = int(input())

for current_number in range(number_first, number_second +1):
    sum_even = 0
    sum_odd = 0
    current_number_str = str(current_number)
    for index, digit in enumerate(current_number_str):
        if index % 2 == 0:
            sum_odd += int(digit)
        elif index % 2 != 0:
            sum_even += int(digit)
    if sum_odd == sum_even:
        print(current_number, end = " ")
