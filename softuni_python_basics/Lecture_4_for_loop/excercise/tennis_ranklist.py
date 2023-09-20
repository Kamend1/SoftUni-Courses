from math import floor
number_tournaments = int(input())
starting_points = int(input())
final_points = starting_points
points_won = 0
number_tournaments_won = 0

for i in range(0, number_tournaments):
    stage_reached = input()
    if stage_reached == "W":
        final_points += 2000
        points_won += 2000
        number_tournaments_won += 1
    elif stage_reached == "F":
        final_points += 1200
        points_won += 1200
    elif    stage_reached == "SF":
        final_points += 720
        points_won += 720

print(f"Final points: {final_points}")
print(f"Average points: {floor(points_won / number_tournaments)}")
print(f"{number_tournaments_won *100 / number_tournaments:.2f}%")
