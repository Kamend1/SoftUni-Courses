from collections import deque

size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
coordinates = deque(input().split())

while coordinates:
    current_bomb = coordinates.popleft()
    current_row = int(current_bomb[0])
    current_col = int(current_bomb[2])
    if matrix[current_row][current_col] > 0:
        current_damage = matrix[current_row][current_col]
    else:
        current_damage = 0
    row = current_row - 1
    col = current_col - 1
    for i in range(3):
        for j in range(3):
            if 0 <= row < size and 0 <= col < size and matrix[row][col] > 0:
                matrix[row][col] -= current_damage
                col += 1
            else:
                col += 1
        row += 1
        col = current_col - 1

number_alive = 0
sum_alive = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            number_alive += 1
            sum_alive += matrix[row][col]

print(
    f"Alive cells: {number_alive}\n"
    f"Sum: {sum_alive}"
)

for list in matrix:
    print(*list)
