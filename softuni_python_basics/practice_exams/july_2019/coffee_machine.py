type_drink = input()
if_sugar = input()
number_drinks = int(input())
price = 0

if type_drink == "Espresso":
    if if_sugar == "Without":
        price = 0.90
    elif if_sugar == "Normal":
        price = 1.00
    elif if_sugar == "Extra":
        price = 1.20
elif type_drink == "Cappuccino":
    if if_sugar == "Without":
        price = 1.00
    elif if_sugar == "Normal":
        price = 1.20
    elif if_sugar == "Extra":
        price = 1.60
elif type_drink == "Tea":
    if if_sugar == "Without":
        price = 0.50
    elif if_sugar == "Normal":
        price = 0.60
    elif if_sugar == "Extra":
        price = 0.70

if if_sugar == "Without":
    price *= 0.65

if type_drink == "Espresso" and number_drinks >= 5:
    price *= 0.75

total_amount = price * number_drinks
if total_amount > 15:
    total_amount *= 0.80

print(f"You bought {number_drinks} cups of {type_drink} for {total_amount:.2f} lv.")
