count_integers = int(input())
number_integers_by_two = 0
number_integers_by_three = 0
number_integers_by_four = 0

for i in range(count_integers):
    current_integer = int(input())
    if current_integer % 2 == 0:
        number_integers_by_two += 1
    if current_integer % 3 == 0:
        number_integers_by_three += 1
    if current_integer % 4 == 0:
        number_integers_by_four += 1

percent_by_two = number_integers_by_two * 100 / count_integers
percent_by_three = number_integers_by_three * 100 / count_integers
percent_by_four = number_integers_by_four * 100 / count_integers

print(f"{percent_by_two:.2f}%")
print(f"{percent_by_three:.2f}%")
print(f"{percent_by_four:.2f}%")
