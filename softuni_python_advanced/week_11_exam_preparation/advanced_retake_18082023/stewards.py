from collections import deque

seats = [x for x in input().split(', ')]
first_seq = deque(int(x) for x in input().split(', '))
second_seq = deque(int(x) for x in input().split(', '))
rotations = 0
matched_seats = []

while True:
    first_number = first_seq.popleft()
    second_number = second_seq.pop()
    rotations += 1
    remove_numbers = False
    result = first_number + second_number
    first_combo = str(first_number) + chr(result)
    second_combo = str(second_number) + chr(result)


    if first_combo in seats:
        seats.remove(first_combo)
        matched_seats.append(first_combo)
        remove_numbers = True

    if second_combo in seats:
        seats.remove(second_combo)
        matched_seats.append(second_combo)
        remove_numbers = True

    if not remove_numbers:
        first_seq.append(first_number)
        second_seq.appendleft(second_number)

    if rotations == 10:
        break

    if len(matched_seats) == 3:
        break
print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")
