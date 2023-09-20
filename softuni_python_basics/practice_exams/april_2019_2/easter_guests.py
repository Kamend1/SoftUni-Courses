from math import ceil
number_guests = int(input())
budget_lyubo = int(input())
price_kozunak = 4.00
price_egg = 0.45
number_kozunaks = ceil(number_guests / 3)
number_eggs = number_guests * 2
amount_needed = number_eggs * price_egg + number_kozunaks * price_kozunak
difference = abs(budget_lyubo - amount_needed)

if budget_lyubo >= amount_needed:
    print(f"Lyubo bought {number_kozunaks} Easter bread and {number_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
