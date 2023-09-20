number_rolls_packing_paper = int(input())
number_rolls_fabric = int(input())
liters_glue = float(input())
percent_discount = int(input())

price_roll_packing_paper = 5.80
price_roll_fabric = 7.20
price_liter_glue =  1.20

amount_packing_paper = number_rolls_packing_paper * price_roll_packing_paper
amount_fabric = number_rolls_fabric * price_roll_fabric
amount_glue = liters_glue * price_liter_glue
total_amount = (amount_packing_paper + amount_fabric + amount_glue) * (1 - percent_discount / 100)

print(f"{total_amount:.3f}")
