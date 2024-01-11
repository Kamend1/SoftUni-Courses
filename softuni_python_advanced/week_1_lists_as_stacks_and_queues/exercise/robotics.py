from collections import deque

robots = input().split(";")
start_time = input().split(":")
start_time_seconds = int(start_time[0]) * 3600 + int(start_time[1]) * 60 + int(start_time[2])

robots_queue = []
for robot in robots:
    robot = robot.split("-")
    robot.append(start_time_seconds)
    robots_queue.append(robot)

part = input()
part_queue = deque()
while part != "End":
    part_queue.append(part)
    part = input()

while len(part_queue) > 0:
    part_taken = False
    current_part = part_queue.popleft()
    start_time_seconds += 1

    for current_robot in robots_queue:
        if current_robot[2] <= start_time_seconds:
            current_robot[2] = start_time_seconds + int(current_robot[1])
            part_taken = True
            time_taken_hours = start_time_seconds // 3600
            if time_taken_hours >= 24:
                time_taken_hours -= 24
            time_taken = f"{time_taken_hours:02d}:{(start_time_seconds % 3600) // 60:02d}:{start_time_seconds % 60:02d}"
            print(f"{current_robot[0]} - {current_part} [{time_taken}]")
            break

    if not part_taken:
        part_queue.append(current_part)
