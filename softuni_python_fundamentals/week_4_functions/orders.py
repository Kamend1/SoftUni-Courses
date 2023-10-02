def order_price(product, quantity):
    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity * 1.00
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2.00
    return result

product = input()
quantity = int(input())
print(f"{order_price(product, quantity):.2f}")
