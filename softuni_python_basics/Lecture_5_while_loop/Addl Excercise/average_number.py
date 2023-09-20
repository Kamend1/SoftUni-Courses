number_inputs = int(input())
sum_numbers = 0
current_cycle_input = 0

while current_cycle_input < number_inputs:
    number = int(input())
    sum_numbers += number
    current_cycle_input += 1

average_number = sum_numbers / number_inputs
print(f"{average_number:.2f}")
