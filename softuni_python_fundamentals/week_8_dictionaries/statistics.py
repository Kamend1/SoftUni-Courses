products = {}

user_command = input()

while user_command != "statistics":
    user_command = user_command.split(": ")
    if user_command[0] not in products:
        product, quantity = user_command[0], user_command[1]
        products[product] = int(quantity)
    else:
        products[user_command[0]] += int(user_command[1])

    user_command = input()

print('Products in stock:')
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
