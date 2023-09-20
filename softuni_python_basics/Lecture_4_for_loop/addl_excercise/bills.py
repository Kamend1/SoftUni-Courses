number_months = int(input())
water_bill = 20
internet_bill = 15
total_electricity = 0
total_water = water_bill * number_months
total_internet = internet_bill * number_months
total_other = 0
total_cost = 0

for months in range(1, number_months + 1):
    electricity_bill = float(input())
    other_cost = 1.20 * (electricity_bill + water_bill + internet_bill)
    total_electricity += electricity_bill
    total_other += other_cost
    total_cost += electricity_bill + other_cost

total_cost += (total_water + total_internet)
average_cost = total_cost / number_months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average_cost:.2f} lv")
