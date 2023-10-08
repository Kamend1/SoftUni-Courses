number_of_rooms = int(input())
room_numbers = []
needed_chairs = []

for room in range(1, number_of_rooms + 1):
    room_numbers.append(room)
    chairs, visitors = input().split()
    current_needed_chairs = len(chairs) - int(visitors)
    needed_chairs.append(current_needed_chairs)

if sum(needed_chairs) < 0:
    for idx in range(len(room_numbers)):
        if needed_chairs[idx] < 0:
            print(f"{-needed_chairs[idx]} more chairs needed in room {room_numbers[idx]}")
else:
    print(f"Game On, {sum(needed_chairs)} free chairs left")
