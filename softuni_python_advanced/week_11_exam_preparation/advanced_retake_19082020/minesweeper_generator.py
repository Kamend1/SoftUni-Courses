def explore_cells(bomb_matrix, cur_row, cur_col):
    counter = 0
    for direction in directions:
        next_row, next_col = cur_row + directions[direction][0], cur_col + directions[direction][1]
        if 0 <= next_row < size and 0 <= next_col < size:
            if bomb_matrix[next_row][next_col] == "*":
                counter += 1

    return counter


size = int(input())
number_bombs = int(input())

matrix = [[0 for _ in range(size)] for _ in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "upleft": (-1, -1),
    "upright": (-1, 1),
    "downleft": (1, -1),
    "downright": (1, 1)
}

for _ in range(number_bombs):
    coords = eval(input())
    row = int(coords[0])
    col = int(coords[1])
    matrix[row][col] = "*"

for row_idx in range(size):
    for col_idx in range(size):
        if matrix[row_idx][col_idx] != "*":
            matrix[row_idx][col_idx] = explore_cells(matrix, row_idx, col_idx)

for line in matrix:
    print(' '.join(str(x) for x in line))
