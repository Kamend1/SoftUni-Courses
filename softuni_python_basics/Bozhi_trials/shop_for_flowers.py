from math import floor, ceil

number_magnolii = int(input())
number_zumbul = int(input())
number_roses = int(input())
number_cactus = int(input())
price_for_present = float(input())

price_magnolii = 3.25 * number_magnolii
price_zumbul = 4 * number_zumbul
price_roses = 3.50 * number_roses
price_cactus = 8 * number_cactus
all_money = (price_zumbul + price_roses + price_cactus + price_magnolii) * 0.95

money_left = floor(abs(price_for_present - all_money))
money_not_enough = ceil(abs(price_for_present - all_money))

if all_money >= price_for_present:
    print(f"She is left with {money_left} leva.")
else:
    print(f"She will have to borrow {money_not_enough}")
