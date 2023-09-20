from math import ceil

name_serial = str(input())
time_epizod = int(input())
time_break = int(input())
time_watch = time_break - time_break / 4 - time_break / 8
time_left = ceil(abs(time_watch - time_epizod))

if time_watch >= time_epizod:
    print(f'You have enough time to watch {name_serial} and left with {time_left} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, you need {time_left} more minutes.")
