import sys
target_profit = float(input())
club_income = 0

for i in range(sys.maxsize):
    name_cocktail = input()
    if name_cocktail == "Party!":
        break
    number_cocktails = int(input())
    price_cocktails = len(name_cocktail)
    income_order = number_cocktails * price_cocktails
    if income_order % 2 != 0:
        income_order *= 0.75
    club_income += income_order
    if club_income >= target_profit:
        break

difference = abs(target_profit - club_income)

if club_income >= target_profit:
    print("Target acquired.")
    print(f"Club income - {club_income:.2f} leva.")
else:
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {club_income:.2f} leva.")
