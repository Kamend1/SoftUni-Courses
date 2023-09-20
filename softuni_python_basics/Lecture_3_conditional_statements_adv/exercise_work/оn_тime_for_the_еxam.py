hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

time_exam_minutes = hour_exam * 60 + minutes_exam
time_arrival_minutes = hour_arrival * 60 + minutes_arrival
difference = abs(time_arrival_minutes - time_exam_minutes)
difference_hours = difference // 60
difference_minutes = difference % 60

if time_arrival_minutes > time_exam_minutes:
    if time_arrival_minutes >= time_exam_minutes + 60:
        print("Late")
        print(f"{difference_hours}:{difference_minutes:02d} hours after the start")
    elif time_arrival_minutes < time_exam_minutes + 60:
        print("Late")
        print(f"{difference_minutes} minutes after the start")
elif time_exam_minutes - 30 <= time_arrival_minutes <= time_exam_minutes:
    print("On time")
    print(f"{difference_minutes} minutes before the start")
elif time_arrival_minutes < time_exam_minutes - 30:
    if time_arrival_minutes <= time_exam_minutes - 60:
        print("Early")
        print(f"{difference_hours}:{difference_minutes:02d} hours before the start")
    else:
        print("Early")
        print(f"{difference_minutes} minutes before the start")
