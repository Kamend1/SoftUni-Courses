name_actor = input()
academy_points = float(input())
number_scorers = int(input())
points_actor = academy_points

for i in range(0, number_scorers):
    name_scorer = input()
    points = float(input())
    points_actor += (points * len(name_scorer) / 2)

    if points_actor > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points_actor:.1f}!")
        break

if points_actor <= 1250.5:
    difference = 1250.5 - points_actor
    print(f"Sorry, {name_actor} you need {difference:.1f} more!")
