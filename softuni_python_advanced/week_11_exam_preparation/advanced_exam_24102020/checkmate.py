def search_direction(current_matrix, row_index, col_index, direction):
    coordinates = directions[direction]
    result = 0
    for i in range(1, 8):
        next_row = row_index + coordinates[0] * i
        next_col = col_index + coordinates[1] * i

        if next_row < 0 or next_col < 0 or next_row >= 7 or next_col >= 7:
            break

        elif current_matrix[next_row][next_col] == "Q":
            break

        elif current_matrix[next_row][next_col] == "K":
            result = 1
            break

    return result

def search_opposite(current_matrix, row_index, col_index, direction):
    result = 0
    coordinates = directions[direction]

    for i in range(1, 8):
        next_row = row_index - coordinates[0] * i
        next_col = col_index - coordinates[1] * i

        if next_row < 0 or next_col < 0 or next_row >= 7 or next_col >= 7:
            break

        elif current_matrix[next_row][next_col] == "Q":
            break

        elif current_matrix[next_row][next_col] == "K":
            result = 1
            break

    return result

rows, cols = 8, 8

board = []
queens = []
queens_true = []

for row in range(rows):
    line = input().split()
    board.append(line)

    for col_idx in range(len(line)):
        if line[col_idx] == 'Q':
            queens.append((row, col_idx))

directions = {
    'up': (-1, 0),
    'left': (0, -1),
    'upleft': (-1, -1),
    'upright': (-1, 1)
}

for queen in queens:
    row, col = queen

    for direct in directions:
        if search_direction(board, row, col, direct) == 1:
            queens_true.append([row, col])
            break
        elif search_opposite(board, row, col, direct) == 1:
            queens_true.append([row, col])
            break

if queens_true:
    for queen in queens_true:
        print(queen)
else:
    print("The king is safe!")
