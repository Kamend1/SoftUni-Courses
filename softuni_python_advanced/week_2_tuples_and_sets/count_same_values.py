numbers = [float(x) for x in input().split()]

unique_numbers = {}

for num in numbers:
    if num not in unique_numbers:
        unique_numbers[num] = 0
    unique_numbers[num] += 1

for number, occurances in unique_numbers.items():
    print(f"{number} - {occurances} times")
