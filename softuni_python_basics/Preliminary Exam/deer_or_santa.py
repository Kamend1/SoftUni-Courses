from math import ceil, floor
number_days_santa_absent = int(input())
food_left_kg = int(input())
first_deer_food_day = float(input())
second_deer_food_day = float(input())
third_deer_food_day = float(input())

first_deer_total_food = number_days_santa_absent * first_deer_food_day
second_deer_total_food = number_days_santa_absent * second_deer_food_day
third_deer_total_food = number_days_santa_absent * third_deer_food_day
total_food_needed = first_deer_total_food + second_deer_total_food + third_deer_total_food
difference = abs((food_left_kg - total_food_needed))

if total_food_needed > food_left_kg:
    print(f"{ceil(difference)} more kilos of food are needed.")
else:
    print(f"{floor(difference)} kilos of food left.")
