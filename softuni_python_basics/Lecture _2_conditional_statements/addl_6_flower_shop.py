from math import floor, ceil

number_magnolii = int(input())
number_zyumbyul = int(input())
number_rose = int(input())
number_cactus = int(input())
price_magnolii = 3.25
price_zyumbyul = 4.00
price_rose = 3.50
price_cactus = 8.00
price_gift = float(input())

amount_order = (number_magnolii * price_magnolii \
               + number_zyumbyul * price_zyumbyul \
               + number_cactus * price_cactus \
               + number_rose * price_rose) * 0.95
amount_left = floor(amount_order - price_gift)
amount_borrowed = ceil(price_gift - amount_order)

if amount_order >= price_gift:
    print(f'She is left with {amount_left} leva.')
else:
    print(f'She will have to borrow {amount_borrowed} leva.')
