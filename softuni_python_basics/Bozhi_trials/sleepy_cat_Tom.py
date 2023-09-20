number_rest_days = int(input())
number_work_days = 365 - number_rest_days
norm_tom_play = 30000
play_rest_days = number_rest_days * 127
play_work_days = number_work_days * 63
total_play_minutes = play_work_days + play_rest_days
difference = abs(norm_tom_play - total_play_minutes)
difference_hours = difference // 60
difference_minutes = difference % 60

if total_play_minutes > norm_tom_play:
    print("Tom will run away")
    print(f"{difference_hours} hours and {difference_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{difference_hours} hours and {difference_minutes} minutes less for play")

