numbers = [int(x) for x in input().split(', ')]
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(str(number))
    else:
        odd_numbers.append(str(number))
    if number >= 0:
        positive_numbers.append(str(number))
    else:
        negative_numbers.append(str(number))

positive_string = ", ".join(positive_numbers)
negative_string = ", ".join(negative_numbers)
even_string = ", ".join(even_numbers)
odd_string = ", ".join(odd_numbers)

print(f"Positive: {positive_string}")
print(f"Negative: {negative_string}")
print(f"Even: {even_string}")
print(f"Odd: {odd_string}")
