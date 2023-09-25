number_persons = int(input())
elevator_capacity = int(input())
result = 0

if number_persons < elevator_capacity:
    result = 1
elif number_persons % elevator_capacity != 0:
    result = number_persons // elevator_capacity + 1
else:
    result = number_persons // elevator_capacity

print(result)
