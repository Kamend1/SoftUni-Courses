number_non_working_days = int(input())
working_days = 365 - number_non_working_days

playing_time = working_days * 63 + number_non_working_days * 127
norm_playing_time = 30000
difference = abs(norm_playing_time - playing_time)
hours_difference = difference // 60
minutes_difference = difference % 60

if norm_playing_time - playing_time <= 0:
    print("Tom will run away")
    print(f"{hours_difference} hours and {minutes_difference} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours_difference} hours and {minutes_difference} minutes less for play")
