from sys import maxsize

player_name = input()
total_points = 301
total_shots = 0
total_successful_shots = 0
total_unsuccessful_shots = 0

for shots in range(maxsize):
    field = input()
    if field == "Retire":
        print(f"{player_name} retired after {total_unsuccessful_shots} unsuccessful shots.")
        break
    elif field == "Triple":
        score = int(input()) * 3
        if score > total_points:
            total_shots += 1
            total_unsuccessful_shots += 1
        else:
            total_points -= score
            total_shots += 1
            total_successful_shots +=1
    elif field == "Double":
        score = int(input()) * 2
        if score > total_points:
            total_shots += 1
            total_unsuccessful_shots += 1
        else:
            total_points -= score
            total_shots += 1
            total_successful_shots += 1
    elif field == "Single":
        score = int(input())
        if score > total_points:
            total_shots += 1
            total_unsuccessful_shots += 1
        else:
            total_points -= score
            total_shots += 1
            total_successful_shots += 1
    if total_points == 0:
        print(f"{player_name} won the leg with {total_successful_shots} shots.")
        break
    else:
        continue
