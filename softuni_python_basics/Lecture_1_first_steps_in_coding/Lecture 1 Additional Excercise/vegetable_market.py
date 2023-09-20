price_veg_kg = float(input())
price_fruit_kg = float(input())
qty_veg_kg = int(input())
qty_fruit_kr = int(input())

total_revenue_bgn = price_veg_kg * qty_veg_kg + price_fruit_kg * qty_fruit_kr
total_revenue_eur = total_revenue_bgn / 1.94

print(f"{total_revenue_eur:.2f}")
