from sys import maxsize

cinema_capacity = int(input())
number_of_people = 0
price = 5
total_income = 0
difference = cinema_capacity

for people in range(cinema_capacity):
    user_input = input()
    if user_input == "Movie time!":
        print(f"There are {difference} seats left in the cinema.")
        break
    if int(user_input) > difference:
        print("The cinema is full.")
        break
    number_of_people += int(user_input)
    total_income += int(user_input) * price
    difference = cinema_capacity - number_of_people
    if int(user_input) % 3 == 0:
        total_income -= 5

print(f"Cinema income - {int(total_income)} lv.")
