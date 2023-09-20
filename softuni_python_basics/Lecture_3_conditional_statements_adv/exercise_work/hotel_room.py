month = str(input())
number_nights = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    if number_nights <= 7:
        price_apartment = 65
        price_studio = 50
    elif 7 < number_nights <= 14:
        price_studio = 50 * 0.95
        price_apartment = 65
    elif number_nights > 14:
        price_studio = 50 * 0.70
        price_apartment = 65 * 0.90
elif month == "June" or month == "September":
    if number_nights <= 14:
        price_apartment = 68.70
        price_studio = 75.20
    elif number_nights > 14:
        price_studio = 75.20 * 0.80
        price_apartment = 68.70 * 0.90
elif month == "July" or month == "August":
    if number_nights <= 14:
        price_apartment = 77
        price_studio = 76
    if number_nights > 14:
        price_apartment = 77 * 0.90
        price_studio = 76

amount_apartment = number_nights * price_apartment
amount_studio = number_nights * price_studio
print(f"Apartment: {amount_apartment:.2f} lv.")
print(f"Studio: {amount_studio:.2f} lv.")
