number_loads = int(input())
total_weight = 0
tonnage_van = 0
tonnage_truck = 0
tonnage_train = 0
total_amount = 0

for _ in range(number_loads):
    load_weight = int(input())
    total_weight += load_weight
    if load_weight <= 3:
        total_amount += load_weight * 200
        tonnage_van += load_weight
    elif load_weight <= 11:
        total_amount += load_weight * 175
        tonnage_truck += load_weight
    elif load_weight >= 12:
        total_amount += load_weight * 120
        tonnage_train += load_weight

average_price_ton = total_amount / total_weight
percentage_tonnage_van = tonnage_van * 100 / total_weight
percentage_tonnage_truck = tonnage_truck * 100 / total_weight
percentage_tonnage_train = tonnage_train * 100 / total_weight

print(f"{average_price_ton:.2f}")
print(f"{percentage_tonnage_van:.2f}%")
print(f"{percentage_tonnage_truck:.2f}%")
print(f"{percentage_tonnage_train:.2f}%")
