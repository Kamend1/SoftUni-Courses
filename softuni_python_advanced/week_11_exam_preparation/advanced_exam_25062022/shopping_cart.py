def shopping_cart(*products):
    added_products = {}
    no_products_added = True
    for product_name in limit_of_products.keys():
        added_products[product_name] = []
    for product in products:
        if product == "Stop":
            break
        if len(added_products[product[0]]) < limit_of_products[product[0]]:
            if product[1] not in added_products[product[0]]:
                added_products[product[0]].append(product[1])
                no_products_added = False

    if not no_products_added:
        sorted_products = dict(sorted(added_products.items(), key=lambda x: (-len(x[1]), x[0])))

        result = ''
        for k, v in sorted_products.items():
            result += f"{k}:\n"
            for product in sorted(v):
                result += f" - {product}\n"
    else:
        result = "No products in the cart!"

    return result

limit_of_products = {
    "Soup": 3,
    "Pizza": 4,
    "Dessert": 2,
}

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
