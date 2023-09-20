time_hours = int(input())
time_minutes = int(input())
time_minutes += 15
time_hours += time_minutes // 60
time_minutes %= 60

if time_hours > 23:
    time_hours = 0

print(f'{time_hours}:{time_minutes:02d}')
