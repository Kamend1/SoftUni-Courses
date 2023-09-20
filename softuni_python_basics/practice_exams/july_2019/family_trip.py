trip_budget = float(input())
number_nights = int(input())
price_night = float(input())
percent_additional = int(input())

if number_nights > 7:
    price_night *= 0.95

money_needed = (number_nights * price_night) + (percent_additional / 100) * trip_budget
difference = abs(trip_budget - money_needed)

if trip_budget >= money_needed:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
