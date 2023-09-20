price_trip = float(input())
qty_puzzles = int(input())
qty_dolls = int(input())
qty_teddy_bears = int(input())
qty_minions = int(input())
qty_trucks = int(input())
price_puzzles = 2.60
price_dolls = 3
price_teddy_bears = 4.10
price_minions = 8.20
price_trucks = 2

number_toys = qty_trucks + qty_dolls \
              + qty_teddy_bears + qty_puzzles \
              + qty_minions
amount_earned = (qty_minions * price_minions) + (qty_trucks * price_trucks)\
    + (qty_dolls * price_dolls) + (qty_puzzles * price_puzzles)\
    + (qty_teddy_bears * price_teddy_bears)
amount_left = 0


if number_toys >= 50:
    amount_left = (0.75 * amount_earned) * 0.9
else:
    amount_left = amount_earned * 0.9

amount_diff = abs(price_trip - amount_left)

if amount_left >= price_trip:
    print(f'Yes! {amount_diff:.2f} lv left.')
else:
    print(f'Not enough money! {amount_diff:.2f} lv needed.')
