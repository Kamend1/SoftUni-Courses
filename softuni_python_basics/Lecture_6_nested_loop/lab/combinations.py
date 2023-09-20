user_input_range = int(input())
counter_combo = 0
for x1 in range(user_input_range + 1):
    for x2 in range(user_input_range + 1):
        for x3 in range(user_input_range + 1):
            sum_numbers = x1 + x2 + x3
            if sum_numbers == user_input_range:
                counter_combo += 1
print(counter_combo)
