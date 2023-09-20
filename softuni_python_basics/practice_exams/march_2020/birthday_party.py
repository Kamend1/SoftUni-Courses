hall_rent = float(input())

cake_price = 0.20 * hall_rent
drinks_price = 0.55 * cake_price
animator = hall_rent / 3

total_budget = hall_rent + cake_price + drinks_price + animator
print(total_budget)
