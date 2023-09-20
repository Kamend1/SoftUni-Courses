number_windows = int(input())
size_windows = input()
type_delivery = input()

if number_windows < 10:
    print("Invalid order")
else:
    price = 0

    if size_windows == "90X130":
        if number_windows > 60:
            price = 110 * 0.92
        elif number_windows > 30:
            price = 110 * 0.95
        else:
            price = 110
    elif size_windows == "100X150":
        if number_windows > 80:
            price = 140 * 0.90
        elif number_windows > 40:
            price = 140 * 0.94
        else:
            price = 140
    elif size_windows == "130X180":
        if number_windows > 50:
            price = 190 * 0.88
        elif number_windows > 20:
            price = 190 * 0.93
        else:
            price = 190
    elif size_windows == "200X300":
        if number_windows > 50:
            price = 250 * 0.86
        elif number_windows > 25:
            price = 250 * 0.91
        else:
            price = 250

    if type_delivery == "With delivery":
        total_amount = (number_windows * price) + 60
    else:
        total_amount = number_windows * price

    if number_windows > 99:
        total_amount *= 0.96

    print(f"{total_amount:.2f} BGN")
