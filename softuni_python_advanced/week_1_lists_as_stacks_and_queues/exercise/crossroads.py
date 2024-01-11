from collections import deque
green_light_time = int(input())
free_window_time = int(input())
car_queue = deque()
cars_passed = []
cars_crashed = False


command = input()

while command != 'END':
    if command == 'green':
        total_pass_time = green_light_time
        while total_pass_time > 0:
            if car_queue:
                current_car = car_queue.popleft()
                cars_passed.append(current_car)
                total_pass_time -= len(current_car)
            else:
                total_pass_time = 0
        if total_pass_time < 0:
            time_available = total_pass_time + free_window_time
            if time_available < 0:
                character_hit = current_car[len(current_car) + time_available]
                print(f"A crash happened!\n{current_car} was hit at {character_hit}.")
                cars_crashed = True
                break
    else:
        car_queue.append(command)
    command = input()

if not cars_crashed:
    print(f"Everyone is safe.\n{len(cars_passed)} total cars passed the crossroads.")
