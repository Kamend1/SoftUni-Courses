budget = float(input())
price_1kg_flour = float(input())
price_1pack_egg = 0.75 * price_1kg_flour
price_1lt_milk = 1.25 * price_1kg_flour
price_loaf = price_1kg_flour + price_1pack_egg + 0.25 * price_1lt_milk

number_of_loaves = 0
colored_eggs = 0
money_left = budget

while money_left > price_loaf:
    number_of_loaves += 1
    colored_eggs += 3
    money_left -= price_loaf
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2


print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} \
eggs and {money_left:.2f}BGN left.")
