budget_movie = float(input())
destination = input()
season = input()
number_days = int(input())
price = 0

if destination == "Dubai":
    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000
elif destination == "Sofia":
    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500
elif destination == "London":
    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250

if destination == "Dubai":
    price *= 0.70

if destination == "Sofia":
    price *= 1.25

total_amount = price * number_days
difference = abs(total_amount - budget_movie)

if budget_movie >= total_amount:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
