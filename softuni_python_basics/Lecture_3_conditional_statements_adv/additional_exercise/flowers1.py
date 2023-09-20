number_hryzantemi = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
is_holiday = input()

price_hryzantemi = 0
price_roses = 0
price_tulips = 0

if season == "Spring" or season == "Summer":
    if is_holiday == "Y":
        price_hryzantemi = 2 * 1.15
        price_roses = 4.10 * 1.15
        price_tulips = 2.50 * 1.15
    elif is_holiday == "N":
        price_hryzantemi = 2
        price_roses = 4.10
        price_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    if is_holiday == "Y":
        price_hryzantemi = 3.75 * 1.15
        price_roses = 4.50 * 1.15
        price_tulips = 4.15 * 1.15
    elif is_holiday == "N":
        price_hryzantemi = 3.75
        price_roses = 4.50
        price_tulips = 4.15

price_bouquet = (
    number_hryzantemi * price_hryzantemi
    + number_tulips * price_tulips
    + number_roses * price_roses
)

if season == "Spring" and number_tulips > 7:
    price_bouquet *= 0.95

if season == "Winter" and number_roses >= 10:
    price_bouquet *= 0.9

if number_roses + number_tulips + number_hryzantemi > 20:
    price_bouquet *= 0.8

final_price = price_bouquet + 2

print(f"{final_price:.2f}")
