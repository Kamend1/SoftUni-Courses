product = str(input())
city = str(input())
quantity = float(input())
price = 0

if city == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
    elif product == "sweets":
        price = 1.45
    else:
        price = 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.30
    else:
        price = 1.50
elif city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.10
    elif product == "sweets":
        price = 1.35
    else:
        price = 1.55

amount = quantity * price

print(amount)
