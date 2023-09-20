number_days = int(input())
qty_food = float(input())
total_food_eaten = 0
total_food_eaten_by_dog = 0
total_food_eaten_by_cat = 0
total_eaten_biscuits = 0

for days in range(1, number_days + 1):
    food_dog = float(input())
    food_cat = float(input())
    total_day_food = food_cat + food_dog
    if days % 3 == 0:
        total_eaten_biscuits += 0.10 * total_day_food
    total_food_eaten_by_dog += food_dog
    total_food_eaten_by_cat += food_cat
    total_food_eaten += total_day_food

percent_food_eaten = total_food_eaten * 100 / qty_food
percent_food_eaten_dog = total_food_eaten_by_dog * 100 / total_food_eaten
percent_food_eaten_cat = total_food_eaten_by_cat * 100 / total_food_eaten

print(f"Total eaten biscuits: {int(total_eaten_biscuits)}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_food_eaten_dog:.2f}% eaten from the dog.")
print(f"{percent_food_eaten_cat:.2f}% eaten from the cat.")
