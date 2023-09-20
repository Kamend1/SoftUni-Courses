number_guests = int(input())
price_per_guest = float(input())
budget_desi = float(input())
price_cake = budget_desi * 0.10

if number_guests > 25:
    price_per_guest *= 0.75
elif 15 < number_guests <= 25:
    price_per_guest *= 0.80
elif 10 <= number_guests <= 15:
    price_per_guest *= 0.85

amount_needed = number_guests * price_per_guest + price_cake
difference = abs(budget_desi - amount_needed)

if budget_desi >= amount_needed:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
