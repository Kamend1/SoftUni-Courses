nylon_quant = int(input())
paint_quant = int(input())
thinner_quant = int(input())
hours = int(input())

nylon_price_sqm = 1.50
paint_price_ltr = 14.50
thinner_price_ltr = 5.00
bag_price = 0.40

materials_amount = (nylon_quant + 2) * nylon_price_sqm \
                   + (paint_quant * 1.1) * paint_price_ltr \
                   + thinner_quant * thinner_price_ltr \
                   + bag_price

labor_cost = 0.3 * materials_amount * hours

total_amount = materials_amount + labor_cost

print(total_amount)
