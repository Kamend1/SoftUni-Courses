size = int(input())
matrix = []
start_position = None
burrows = []
food_quantity = 0

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

for row in range(size):
    line = list(input())
    matrix.append(line)

    for el in line:
        if el == 'S':
            start_position = (row, line.index('S'))
        elif el == 'B':
            burrows.append((row, line.index('B')))

row, col = start_position

while True:
    direction = input()
    next_row, next_col = row + directions[direction][0], col + directions[direction][1]

    if not 0 <= next_row < size or not 0 <= next_col < size:
        print("Game over!")
        matrix[row][col] = "."
        break
    else:
        symbol = matrix[next_row][next_col]

    if symbol == "*":
        food_quantity += 1
        matrix[row][col] = "."
        row, col = next_row, next_col
        matrix[row][col] = "S"
    elif symbol == "B":
        matrix[row][col] = "."
        row, col = next_row, next_col
        matrix[row][col] = "."
        burrows.remove((row, col))
        row, col = burrows[0]
        matrix[row][col] = "S"
    elif symbol == "-":
        matrix[row][col] = "."
        row, col = next_row, next_col
        matrix[row][col] = "S"

    if food_quantity >= 10:
        print(f"You won! You fed the snake.")
        break

print(f"Food eaten: {food_quantity}")

for line in matrix:
    print(''.join(line))
