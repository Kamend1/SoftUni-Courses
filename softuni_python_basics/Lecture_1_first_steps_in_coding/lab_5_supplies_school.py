number_of_pens = int(input())
number_of_markers = int(input())
liters_detergent = int(input())
percent_discount = int(input())

price_per_pen = 5.80
price_per_marker = 7.20
price_per_liter_detergent = 1.20

amount_pens = number_of_pens * price_per_pen
amount_markers = number_of_markers * price_per_marker
amount_detergent = liters_detergent * price_per_liter_detergent
amount_total = amount_pens + amount_markers + amount_detergent

amount_final = amount_total - (amount_total * (percent_discount/100))

print(amount_final)
