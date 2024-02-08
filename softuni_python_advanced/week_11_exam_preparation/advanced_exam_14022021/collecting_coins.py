from math import floor

size = int(input())
matrix = []
path = []
coins = 0

for row in range(size):
    line = input().split()
    matrix.append(line)

    if 'P' in line:
        start_row = row
        start_col = line.index('P')

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

row, col = start_row, start_col
path.append([row, col])
matrix[row][col] = 0

while True:
    command = input()
    row += directions[command][0]
    col += directions[command][1]

    if row < 0:
        row = size - 1

    if row == size:
        row = 0

    if col < 0:
        col = size - 1

    if col == size:
        col = 0

    if matrix[row][col] == 'X':
        path.append([row, col])
        coins = floor(coins / 2)
        print(f"Game over! You've collected {coins} coins.")
        break
    else:
        path.append([row, col])
        coins += int(matrix[row][col])
        matrix[row][col] = 0
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break

print("Your path:")
print(*path, sep="\n")
