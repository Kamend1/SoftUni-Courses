number_days = int(input())
number_hours = int(input())
amount_parking = 0
amount_per_day = 0

for day in range(1, number_days + 1):
    for hour in range(1, number_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            amount_parking += 2.50
            amount_per_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            amount_parking += 1.25
            amount_per_day += 1.25
        else:
            amount_parking += 1
            amount_per_day += 1
    print(f"Day: {day} - {amount_per_day:.2f} leva")
    amount_per_day = 0
print(f"Total: {amount_parking:.2f} leva")
