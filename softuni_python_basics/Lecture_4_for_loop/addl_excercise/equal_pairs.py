import sys
numbers = int(input())
max_diff = -sys.maxsize
previous_sum = 0
all_equal = True

for i in range(numbers):
    first_number = int(input())
    second_number = int(input())
    sum_pair = first_number + second_number
    if previous_sum !=0 and sum_pair != previous_sum:
        all_equal = False
        difference = abs(sum_pair - previous_sum)
        if difference > max_diff:
            max_diff = difference

    previous_sum = sum_pair

if all_equal == True:
    print(f"Yes, value={sum_pair}")
else:
    print(f"No, maxdiff={max_diff}")
