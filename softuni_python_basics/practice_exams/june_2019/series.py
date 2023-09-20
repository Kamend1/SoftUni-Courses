budget = float(input())
number_serials = int(input())
amount_needed = 0

for i in range(number_serials):
    name_serial = input()
    price_serial = float(input())
    if name_serial == "Thrones":
        price_serial *= 0.50
    elif name_serial == "Lucifer":
        price_serial *= 0.60
    elif name_serial == "Protector":
        price_serial *= 0.70
    elif name_serial == "TotalDrama":
        price_serial *= 0.80
    elif name_serial == "Area":
        price_serial *= 0.90

    amount_needed += price_serial

difference = abs(budget - amount_needed)
if budget >= amount_needed:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")
