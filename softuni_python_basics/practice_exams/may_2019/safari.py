budget_safari = float(input())
fuel_needed_liters = float(input())
day_week = str(input())

price_fuel_liter = 2.10
price_guide = 100

if day_week == "Saturday":
    amount_needed = 0.90 * (fuel_needed_liters * price_fuel_liter + price_guide)
else:
    amount_needed = 0.80 * (fuel_needed_liters * price_fuel_liter + price_guide)

difference = abs(budget_safari - amount_needed)

if amount_needed <= budget_safari:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
