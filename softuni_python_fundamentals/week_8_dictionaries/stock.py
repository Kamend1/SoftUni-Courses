data_input = input().split()
stock = {}

for i in range(0, len(data_input), 2):
    key, value = data_input[i], data_input[i + 1]
    stock[key] = int(value)

products_to_search = input().split()

for product in products_to_search:
    if product in stock.keys():
        print(f"We have {stock.get(product)} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
