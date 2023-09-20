from math import floor, ceil
price_tennis_raquet = float(input())
number_tennis_raquet = int(input())
number_shoe_pairs = int(input())
price_shoe_pair = price_tennis_raquet / 6
amount_needed = price_shoe_pair * number_shoe_pairs \
                + price_tennis_raquet * number_tennis_raquet
total_amount_needed = amount_needed + amount_needed * 0.20
amount_player = floor((1 * total_amount_needed) / 8)
amount_sponsor = ceil((7 * total_amount_needed) / 8)

print(f"Price to be paid by Djokovic {amount_player}")
print(f"Price to be paid by sponsors {amount_sponsor}")
