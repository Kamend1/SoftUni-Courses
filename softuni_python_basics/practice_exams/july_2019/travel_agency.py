name_town = input()
type_package = input()
is_vip = input()
number_nights = int(input())
price = 0

if name_town == "Bansko" or name_town == "Borovets":
    if type_package == "withEquipment":
        price = 100
    elif type_package == "noEquipment":
        price = 80
elif name_town == "Varna" or name_town == "Burgas":
    if type_package == "withBreakfast":
        price = 130
    elif type_package == "noBreakfast":
        price = 100

if is_vip == "yes" and (name_town == "Bansko" or name_town == "Borovets"):
    if type_package == "withEquipment":
        price *= 0.90
    elif type_package == "noEquipment":
        price *= 0.95

if is_vip == "yes" and (name_town == "Varna" or name_town == "Burgas"):
    if type_package == "withBreakfast":
        price *= 0.88
    elif type_package == "noBreakfast":
        price *= 0.93

if number_nights < 1:
    print("Days must be positive number!")
elif name_town != "Bansko" and name_town != "Borovets" \
        and name_town != "Varna" and name_town != "Burgas":
    print("Invalid input!")
elif type_package != "withEquipment" and type_package != "noBreakfast" \
        and type_package != "noEquipment" and type_package != "withBreakfast":
    print("Invalid input!")
else:
    if number_nights > 7:
        total_amount = (number_nights - 1) * price
        print(f"The price is {total_amount:.2f}lv! Have a nice time!")
    else:
        total_amount = number_nights * price
        print(f"The price is {total_amount:.2f}lv! Have a nice time!")
