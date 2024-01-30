from collections import deque

time_for_task = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

ducks = {'Darth Vader Ducky': 0,
         'Thor Ducky': 0,
         'Big Blue Rubber Ducky': 0,
         'Small Yellow Rubber Ducky': 0,
}

while time_for_task and number_of_tasks:
    current_time = time_for_task.popleft()
    current_tasks = number_of_tasks.pop()
    result = current_time * current_tasks

    if result <= 60:
        ducks['Darth Vader Ducky'] += 1
    elif 61 <= result <= 120:
        ducks['Thor Ducky'] += 1
    elif 121 <= result <= 180:
        ducks['Big Blue Rubber Ducky'] += 1
    elif 181 <= result <= 240:
        ducks['Small Yellow Rubber Ducky'] += 1
    else:
        time_for_task.append(current_time)
        number_of_tasks.append(current_tasks - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for k, v in ducks.items():
    print(f"{k}: {v}")
