from math import floor, ceil

number_of_days = int(input())
amount_food_kg = int(input())
food_dog_day_kg = float(input())
food_cat_day_kg = float(input())
food_turtle_day_gr = float(input())
amount_food_dog_kg = food_dog_day_kg * number_of_days
amount_food_cat_kg = food_cat_day_kg * number_of_days
amount_food_turtle_kg = food_turtle_day_gr * number_of_days / 1000
total_food_needed = amount_food_dog_kg + amount_food_cat_kg + amount_food_turtle_kg
difference_down = floor(abs(amount_food_kg - total_food_needed))
differnece_up = ceil(abs(amount_food_kg - total_food_needed))

if amount_food_kg - total_food_needed >= 0:
    print(f"{difference_down} kilos of food left.")
else:
    print(f"{differnece_up} more kilos of food are needed.")
