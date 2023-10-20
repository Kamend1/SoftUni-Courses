orders = {}

user_command = input().split()

while user_command[0] != "buy":
    product, price, quantity = user_command[0], float(user_command[1]), int(user_command[2])
    if product not in orders:
        orders[product] = {"price": 0, 'quantity': 0}
    orders[product]["quantity"] += quantity
    orders[product]["price"] = price
    user_command = input().split()

for product, attributes in orders.items():
    total_price = orders[product]["price"] * orders[product]["quantity"]
    print(f"{product} -> {total_price:.2f}")
