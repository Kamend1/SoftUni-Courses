season = input()
number_km = float(input())
price_km = 0

if 10000 < number_km <= 20000:
    price_km = 1.45
elif 5000 < number_km <= 10000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.95
    elif season == "Summer":
        price_km = 1.10
    elif season == "Winter":
        price_km = 1.25
elif number_km <= 5000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.75
    elif season == "Summer":
        price_km = 0.90
    elif season == "Winter":
        price_km = 1.05

payment_driver = 0.90 * (number_km * price_km) * 4
print(f"{payment_driver:.2f}")
