budget_group = int(input())
season = input()
number_fishermen = int(input())
price_boat = 0
if season == "Spring":
    price_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600
if number_fishermen <= 6:
    price_boat *= 0.90
elif number_fishermen <= 11:
    price_boat *= 0.85
else:
    price_boat *= 0.75
if number_fishermen % 2 == 0 and season != "Autumn":
    price_boat *= 0.95
difference = abs(price_boat - budget_group)
if budget_group >= price_boat:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

