import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
number_barcodes = int(input())

for _ in range(number_barcodes):
    string = input()
    product_group = ""
    if re.match(pattern, string):
        for char in string:
            if char.isdigit():
                product_group += char
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
