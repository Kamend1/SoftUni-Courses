time_hours = int(input())
time_minutes = int(input())

if time_minutes >= 45:
    time_minutes = (time_minutes - 60) + 15
    if time_hours == 23:
        time_hours = 0
    else:
        time_hours += 1
else:
    time_minutes += 15

if time_minutes < 10:
    print(f"{time_hours}:0{time_minutes}")
else:
    print(f"{time_hours}:{time_minutes}")
