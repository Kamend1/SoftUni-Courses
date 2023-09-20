minutes_per_walk = int(input())
number_walks_day = int(input())
calorie_intake = int(input())

calorie_burn = minutes_per_walk * number_walks_day * 5

if calorie_burn >= 0.50 * calorie_intake:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calorie_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calorie_burn}.")
