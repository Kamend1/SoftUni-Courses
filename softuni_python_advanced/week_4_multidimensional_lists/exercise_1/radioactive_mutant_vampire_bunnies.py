from collections import deque

def find_player_starting_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'P':
                return row, col


def check_status(matrix, matrix_row, matrix_col, matrix_rows, matrix_cols):
    status = ""
    bool_var = False
    if matrix_row < 0 or matrix_row == matrix_rows:
        status = 'won'
        bool_var = True
    elif matrix_col < 0 or matrix_col == matrix_cols:
        status = 'won'
        bool_var = True
    elif matrix[matrix_row][matrix_col] == 'B':
        status = 'dead'
        bool_var = True
    return status, bool_var


def handle_player_movement(matrix_command, matrix_row, matrix_col):
    new_row, new_col = matrix_row, matrix_col

    if matrix_command == 'L':
        new_col -= 1
    elif matrix_command == 'R':
        new_col += 1
    elif matrix_command == 'U':
        new_row -= 1
    elif matrix_command == 'D':
        new_row += 1
    return new_row, new_col


def update_bomb_coordinates(matrix, matrix_rows, matrix_cols):
    coordinates = deque()
    for row in range(matrix_rows):
        for col in range(matrix_cols):
            if matrix[row][col] == 'B':
                coordinates.append((row, col))
    return coordinates


def update_field(matrix, matrix_row, matrix_col, matrix_command, status):
    if status == 'dead':
        player_coordinates = (matrix_row, matrix_col)
        if matrix_command == 'L':
            matrix[matrix_row][matrix_col + 1] = "."
        elif matrix_command == 'R':
            matrix[matrix_row][matrix_col - 1] = "."
        elif matrix_command == 'U':
            matrix[matrix_row + 1][matrix_col] = "."
        elif matrix_command == 'D':
            matrix[matrix_row - 1][matrix_col] = "."
    elif status == 'won':
        if matrix_command == 'L':
            player_coordinates = (matrix_row, matrix_col + 1)
            matrix[matrix_row][matrix_col + 1] = "."
        elif matrix_command == 'R':
            player_coordinates = (matrix_row, matrix_col - 1)
            matrix[matrix_row][matrix_col - 1] = "."
        elif matrix_command == 'U':
            player_coordinates = (matrix_row + 1, matrix_col)
            matrix[matrix_row + 1][matrix_col] = "."
        elif matrix_command == 'D':
            player_coordinates = (matrix_row - 1, matrix_col)
            matrix[matrix_row - 1][matrix_col] = "."
    else:
        player_coordinates = (None, None)
        if matrix_command == 'L':
            matrix[matrix_row][matrix_col] = "P"
            matrix[matrix_row][matrix_col + 1] = "."
        elif matrix_command == 'R':
            matrix[matrix_row][matrix_col] = "P"
            matrix[matrix_row][matrix_col - 1] = "."
        elif matrix_command == 'U':
            matrix[matrix_row][matrix_col] = "P"
            matrix[matrix_row + 1][matrix_col] = "."
        elif matrix_command == 'D':
            matrix[matrix_row][matrix_col] = "P"
            matrix[matrix_row - 1][matrix_col] = "."
    return matrix, player_coordinates


rows, cols = map(int, input().split())
field = [[char for char in input()] for _ in range(rows)]

command_string = input()
commands = deque()
for char in command_string:
    commands.append(char)

game_over = False
status_player = ""
last_player_coordinates = (None, None)
current_row,current_col = find_player_starting_position(field)

while commands:
    current_command = commands.popleft()
    current_row, current_col = handle_player_movement(current_command, current_row, current_col)
    status_player, game_over = check_status(field, current_row, current_col, rows, cols)
    field, last_player_coordinates = update_field(field, current_row, current_col, current_command, status_player)

    bomb_coordinates = update_bomb_coordinates(field, rows, cols)

    while bomb_coordinates:
        row, col = bomb_coordinates.popleft()
        if 0 <= row - 1 and field[row - 1][col] == 'P':
            status_player = 'dead'
            last_player_coordinates = (row - 1, col)
            field[row - 1][col] = "B"
            game_over = True
        elif 0 <= row - 1:
            field[row - 1][col] = "B"

        if row + 1 < rows and field[row + 1][col] == 'P':
            status_player = 'dead'
            last_player_coordinates = (row + 1, col)
            field[row + 1][col] = "B"
            game_over = True
        elif row + 1 < rows:
            field[row + 1][col] = "B"

        if 0 <= col -1 and field[row][col - 1] == 'P':
            status_player = 'dead'
            last_player_coordinates = (row, col - 1)
            field[row][col - 1] = "B"
            game_over = True
        elif 0 <= col -1:
            field[row][col - 1] = "B"

        if col + 1 < cols and field[row][col + 1] == 'P':
            status_player = 'dead'
            last_player_coordinates = (row, col + 1)
            field[row][col + 1] = "B"
            game_over = True
        elif col + 1 < cols:
            field[row][col + 1] = "B"

    if game_over:
        break

for list in field:
    print(*list, sep='')
last_row, last_col = last_player_coordinates
print(f"{status_player}: {last_row} {last_col}")
