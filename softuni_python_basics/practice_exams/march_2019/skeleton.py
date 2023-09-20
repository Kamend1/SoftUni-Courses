minutes_control = int(input())
seconds_control = int(input())
length_track = float(input())
seconds_per_100meters = int(input())
control_time_seconds = minutes_control * 60 + seconds_control
time_martin_seconds = (length_track / 100) * seconds_per_100meters - (length_track / 120) * 2.5
difference_time = abs(control_time_seconds - time_martin_seconds)

if time_martin_seconds <= control_time_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {time_martin_seconds:.3f}.')
else:
    print(f'No, Marin failed! He was {difference_time:.3f} second slower.')
