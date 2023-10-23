from math import ceil

budget = float(input())
number_students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())
qty_flour = number_students
qty_eggs = number_students * 10
qty_aprons = ceil(number_students * 1.2)
flour_budget = 0
for i in range(1, number_students + 1):
    if i % 5 == 0:
        continue
    else:
        flour_budget += price_flour
egg_budget = price_egg * qty_eggs
apron_budget = price_apron * qty_aprons
needed_budget = flour_budget + egg_budget + apron_budget
difference_budget = abs(budget - needed_budget)

if budget >= needed_budget:
    print(f"Items purchased for {needed_budget:.2f}$.")
else:
    print(f"{difference_budget:.2f}$ more needed.")
