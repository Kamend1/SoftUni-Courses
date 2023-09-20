name_product = str(input())

if name_product == "banana" or name_product == "apple" or name_product == "kiwi" \
        or name_product == "cherry" or name_product == "lemon" \
        or name_product == "grapes":
    print("fruit")
elif name_product == "tomato" or name_product == "cucumber" or name_product == "pepper" \
        or name_product == "carrot":
    print("vegetable")
else:
    print("unknown")
