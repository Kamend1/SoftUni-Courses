number_kozunak = int(input())
number_egg_carton = int(input())
number_cookie_kg = int(input())
number_egg_paint = number_egg_carton * 12
price_kozunak = 3.20
price_egg_carton =  4.35
price_cookie_kg = 5.40
price_egg_paint = 0.15
amount_needed = number_kozunak * price_kozunak \
                + number_egg_carton * price_egg_carton \
                + number_cookie_kg * price_cookie_kg \
                + number_egg_paint * price_egg_paint

print(f"{amount_needed:.2f}")
