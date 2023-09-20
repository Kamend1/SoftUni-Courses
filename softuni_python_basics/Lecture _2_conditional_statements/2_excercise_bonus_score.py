starting_points = int(input())
bonus_points = 0

if starting_points <= 100:
    bonus_points += 5
elif 100 < starting_points <= 1000:
        bonus_points = 0.2 * starting_points
else:
    bonus_points = 0.1 * starting_points

if starting_points % 2 == 0:
    bonus_points += 1
elif starting_points % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(starting_points + bonus_points)
