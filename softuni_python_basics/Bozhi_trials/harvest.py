from math import floor, ceil

area_vineyard = int(input())
grapes_per_sqm_kg = float(input())
liters_wine_needed = int(input())
number_workers = int(input())
total_harvest_kg = grapes_per_sqm_kg * area_vineyard
harvest_for_wine_kg = total_harvest_kg * 0.40
liters_wine_produced = (harvest_for_wine_kg / 2.5000)
difference_needed = floor((liters_wine_needed - liters_wine_produced))
difference_left = ceil(abs(liters_wine_needed - liters_wine_produced))
liters_worker = ceil((liters_wine_produced - liters_wine_needed) / number_workers)

if liters_wine_produced < liters_wine_needed:
    print(f"It will be a tough winter. More {difference_needed} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {liters_wine_produced} liters.")
    print(f"{difference_left} liters left -> {liters_worker} liters per person.")
