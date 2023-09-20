day_week = str(input())

if day_week == "Saturday" or day_week == "Sunday":
    print("Weekend")
elif day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday" \
        or day_week == "Thursday" or day_week == "Friday":
    print("Working day")
else:
    print("Error")
