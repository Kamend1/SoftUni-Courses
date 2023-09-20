# options: "Roses", "Dahlias", "Tulips", "Narcissus" or "Gladiolus"
type_flower = str(input())
number_flowers = int(input())
budget = int(input())
amount = 0
if type_flower == "Roses":
     if number_flowers > 80:
         amount = number_flowers * 5 * 0.90
     else:
         amount = number_flowers * 5.00
if type_flower == "Dahlias":
    if number_flowers > 90:
        amount = number_flowers * 3.80 * 0.85
    else:
        amount = number_flowers * 3.80
if type_flower == "Tulips":
    if number_flowers > 80:
        amount = number_flowers * 2.80 * 0.85
    else:
        amount = number_flowers * 2.80
if type_flower == "Narcissus":
    if number_flowers >= 120:
        amount = number_flowers * 3
    else:
        amount = number_flowers * 3 * 1.15
if type_flower == "Gladiolus":
    if number_flowers >= 80:
        amount = number_flowers * 2.50
    else:
        amount = number_flowers * 2.50 * 1.20

difference = abs(budget - amount)

if budget >= amount:
    print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
