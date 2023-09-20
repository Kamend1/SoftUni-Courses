amount_to_return = float(input())
total_amount_returned = 0
number_coins = 0
difference = amount_to_return - total_amount_returned

while difference > 0.00:
    if difference >= 2.00:
        total_amount_returned += 2.00
        number_coins += 1
    elif difference >= 1.00:
        total_amount_returned += 1.00
        number_coins += 1
    elif difference >= 0.50:
        total_amount_returned += 0.50
        number_coins += 1
    elif difference >= 0.20:
        total_amount_returned += 0.20
        number_coins += 1
    elif difference >= 0.10:
        total_amount_returned += 0.10
        number_coins += 1
    elif difference >= 0.05:
        total_amount_returned += 0.05
        number_coins += 1
    elif difference >= 0.02:
        total_amount_returned += 0.02
        number_coins += 1
    elif difference >= 0.01:
        total_amount_returned += 0.01
        number_coins += 1
    difference = round(amount_to_return - total_amount_returned, 2)
print(number_coins)
