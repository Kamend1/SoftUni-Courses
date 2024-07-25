budget_of_the_group = int(input())
season_type = str(input())
number_of_people = int(input())

discount = 0
whole_price = 0

if number_of_people <= 6:
    discount = 0.1
elif 7 <= number_of_people <= 11:
    discount = 0.15
else:
    discount = 0.25

if number_of_people % 2 == 0 and season_type != "Autumn":
    discount += 0.05

if season_type == "Summer" or season_type == "Autumn":
    whole_price = 4200 - 4200 * discount
elif season_type == "Spring":
    whole_price = 3000 - 3000 * discount
elif season_type == "Winter":
    whole_price = 2600 - 2600 * discount

difference = abs(budget_of_the_group - whole_price)

if budget_of_the_group >= whole_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
