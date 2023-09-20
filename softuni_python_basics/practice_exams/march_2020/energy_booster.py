type_fruit = input()
size_set = input()
number_sets = int(input())
price = 0
total_amount = 0

if type_fruit == "Watermelon":
    if size_set == "small":
        price = 56.00
    elif size_set == "big":
        price = 28.70
elif type_fruit == "Mango":
    if size_set == "small":
        price = 36.66
    elif size_set == "big":
        price = 19.60
elif type_fruit == "Pineapple":
    if size_set == "small":
        price = 42.10
    elif size_set == "big":
        price = 24.80
elif type_fruit == "Raspberry":
    if size_set == "small":
        price = 20
    elif size_set == "big":
        price = 15.20

if size_set == "small":
    total_amount = price * number_sets * 2
elif size_set == "big":
    total_amount = price * number_sets * 5

if total_amount > 1000:
    total_amount *= 0.50
elif total_amount >= 400:
    total_amount *= 0.85

print(f"{total_amount:.2f} lv.")


