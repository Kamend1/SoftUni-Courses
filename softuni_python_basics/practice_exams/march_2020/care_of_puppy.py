amount_purchased_food_kg = int(input())
user_command = input()
total_food_eaten = 0

while user_command != "Adopted":
    food_eaten = int(user_command)
    total_food_eaten += food_eaten

    user_command = input()

difference = amount_purchased_food_kg * 1000 - total_food_eaten

if difference >= 0:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {abs(difference)} grams more.")
