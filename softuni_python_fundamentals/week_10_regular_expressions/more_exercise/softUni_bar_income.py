import re

string = input()
pattern = r"\%(?P<name>[A-Z][a-z]+)\%[^\d\|\%\$\.]*\<(?P<product>\w+)\>[^\d\|\%\$\.]*\|(?P<quantity>\d+)\|[^\d\|\%\$\.]*(?P<price>\d+\.?\d+)\$"
total_income = 0

while string != 'end of shift':
    match = re.search(pattern, string)
    if match:
        name, product, quantity, price = match.groups()
        total_price = int(quantity) * float(price)
        total_income += total_price
        print(f"{name}: {product} - {total_price:.2f}")
    string = input()

print(f"Total income: {total_income:.2f}")
