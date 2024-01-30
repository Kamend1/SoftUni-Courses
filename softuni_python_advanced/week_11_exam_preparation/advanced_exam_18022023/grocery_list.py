def shop_from_grocery_list(budget, grocery_list, *prices):
    for product, price in prices:
        if product in grocery_list:
            if budget >= price:
                budget -= price
                grocery_list.remove(product)
            else:
                break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

