inherited_amount = float(input())
year_to_live_to = int(input())

number_odd_birthdays = 0
age = 18 - 1
amount_spent = 0

for birthday in range(1800, year_to_live_to + 1):
    age += 1
    if birthday % 2 == 0:
        amount_spent += 12000
    elif birthday % 2 != 0:
        number_odd_birthdays += 1
        amount_spent += 12000 + 50 * age

difference = abs(inherited_amount - amount_spent)

if inherited_amount >= amount_spent:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")
