from math import floor, ceil

number_days = int(input())
kg_food = int(input())
food_day_dog_kg = float(input())
food_cat_day_kg = float(input())
food_day_turtle_gram = float(input())
all_food_for_all_pets = ((food_day_turtle_gram * number_days) / 1000) \
                        + (food_day_dog_kg * number_days) \
                        + (food_cat_day_kg * number_days)
kg_food_left = floor(kg_food - all_food_for_all_pets)
kg_food_not_enough = ceil(all_food_for_all_pets - kg_food)

if kg_food >= all_food_for_all_pets:
    print(f"{kg_food_left} kilos of food left.")
else:
    print(f"{kg_food_not_enough} more kilos of food are needed.")
