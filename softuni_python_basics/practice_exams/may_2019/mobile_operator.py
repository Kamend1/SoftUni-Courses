term_contract = input()
type_contract = input()
add_mobile_internet = input()
number_months = int(input())
price = 0

if type_contract == "Small":
    if term_contract == "one":
        price = 9.98
    elif term_contract == "two":
        price = 8.58
elif type_contract == "Middle":
    if term_contract == "one":
        price = 18.99
    elif term_contract == "two":
        price = 17.09
elif type_contract == "Large":
    if term_contract == "one":
        price = 25.98
    elif term_contract == "two":
        price = 23.59
elif type_contract == "ExtraLarge":
    if term_contract == "one":
        price = 35.99
    elif term_contract == "two":
        price = 31.79

if add_mobile_internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if term_contract == "two":
    price *= 0.9625

total_paid = number_months * price

print(f"{total_paid:.2f} lv.")
