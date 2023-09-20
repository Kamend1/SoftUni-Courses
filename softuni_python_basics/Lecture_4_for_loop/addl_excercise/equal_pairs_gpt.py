n = int(input())

previous_sum = 0
max_difference = 0
all_equal = True

for _ in range(n):
    num1 = int(input())
    num2 = int(input())
    current_sum = num1 + num2

    if previous_sum != 0 and previous_sum != current_sum:
        all_equal = False
        difference = abs(current_sum - previous_sum)
        if difference > max_difference:
            max_difference = difference

    previous_sum = current_sum

if all_equal:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")
