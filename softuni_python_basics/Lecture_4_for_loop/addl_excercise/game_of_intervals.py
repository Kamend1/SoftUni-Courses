numer_of_given_numbers = int(input())
zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_twenty_nine = 0
thirty_to_thirty_nine = 0
forty_to_fifty = 0
invalid_numbers = 0
total_score = 0

for _ in range(numer_of_given_numbers):
    number = int(input())
    if 0 <= number <= 9:
        total_score += number * 0.20
        zero_to_nine += 1
    elif 10 <= number <= 19:
        total_score += number * 0.30
        ten_to_nineteen += 1
    elif 20 <= number <= 29:
        total_score += number * 0.40
        twenty_to_twenty_nine += 1
    elif 30 <= number <= 39:
        total_score += 50
        thirty_to_thirty_nine += 1
    elif 40 <= number <= 50:
        total_score += 100
        forty_to_fifty += 1
    else:
        total_score /= 2
        invalid_numbers += 1

percent_zero_to_nine = zero_to_nine * 100 / numer_of_given_numbers
percent_ten_to_nineteen = ten_to_nineteen * 100 / numer_of_given_numbers
percent_twenty_to_twenty_nine = twenty_to_twenty_nine * 100 / numer_of_given_numbers
percent_thirty_to_thirty_nine = thirty_to_thirty_nine * 100 / numer_of_given_numbers
percent_forty_to_fifty = forty_to_fifty * 100 / numer_of_given_numbers
percent_invalid_numbers = invalid_numbers * 100 / numer_of_given_numbers

print(f"{total_score:.2f}")
print(f"From 0 to 9: {percent_zero_to_nine:.2f}%")
print(f"From 10 to 19: {percent_ten_to_nineteen:.2f}%")
print(f"From 20 to 29: {percent_twenty_to_twenty_nine:.2f}%")
print(f"From 30 to 39: {percent_thirty_to_thirty_nine:.2f}%")
print(f"From 40 to 50: {percent_forty_to_fifty:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")
