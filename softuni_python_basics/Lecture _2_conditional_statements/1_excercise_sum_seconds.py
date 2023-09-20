time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes_time = total_time // 60
seconds_time = total_time % 60

from math import floor

minutes = floor(minutes_time)

if seconds_time < 10:
    print(f"{minutes}:0{seconds_time}")
else:
    print(f"{minutes}:{seconds_time}")
