import sys

number_eggs_first = int(input())
number_eggs_second = int(input())

for i in range(sys.maxsize):
    winner_input = input()
    if winner_input == "End":
        break
    if winner_input == "one":
        number_eggs_second -= 1
    elif winner_input == "two":
        number_eggs_first -= 1
    if number_eggs_first == 0 or number_eggs_second == 0:
        break

if number_eggs_first == 0:
    print(f"Player one is out of eggs. Player two has {number_eggs_second} eggs left.")
elif number_eggs_second == 0:
    print(f"Player two is out of eggs. Player one has {number_eggs_first} eggs left.")
else:
    print(f"Player one has {number_eggs_first} eggs left.")
    print(f"Player two has {number_eggs_second} eggs left.")
