from math import floor, ceil

area_vineyard = int(input())
kg_grapes_1sqm = float(input())
liters_wine_needed = int(input())
number_workers = int(input())

qty_grapes_wine = (area_vineyard * kg_grapes_1sqm) * 0.40
liters_wine_produced = qty_grapes_wine / 2.5
rounded_liters_produced = floor(liters_wine_produced)
difference_liters = floor(abs(liters_wine_needed - liters_wine_produced))
rounded_up_difference = ceil(difference_liters)
liters_per_worker = ceil(rounded_up_difference / number_workers)

if liters_wine_produced - liters_wine_needed < 0:
    print(f'It will be a tough winter! More {difference_liters} liters wine needed.')
else:
    print(f"Good harvest this year! Total wine: {rounded_liters_produced} liters.")
    print(f'{rounded_up_difference} liters left -> {liters_per_worker} liters per person.')
