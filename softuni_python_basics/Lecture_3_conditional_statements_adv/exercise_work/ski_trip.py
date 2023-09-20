number_days = int(input())
type_of_room = str(input())
evaluation = str(input())
price_room = 0

if type_of_room == "room for one person":
    price_room = 18
elif type_of_room == "apartment":
    if number_days > 15:
        price_room = 25 * 0.50
    elif number_days < 10:
        price_room = 25 * 0.70
    else:
        price_room = 25 * 0.65
elif type_of_room == "president apartment":
    if number_days > 15:
        price_room = 35 * 0.80
    elif number_days < 10:
        price_room = 35 * 0.90
    else:
        price_room = 35 * 0.85

if evaluation == "positive":
    price_room *= 1.25
else:
    price_room *= 0.90

amount_spent = price_room * (number_days - 1)

print(f"{amount_spent:.2f}")
