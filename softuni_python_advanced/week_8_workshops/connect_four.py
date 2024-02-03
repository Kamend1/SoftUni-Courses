from collections import deque
import copy


class ColumnFullError(Exception):
    pass


class InvalidColumnInput(Exception):
    pass


class FieldFullError(Exception):
    pass


ROWS = 6
COLUMNS = 7
COLUMNS_HEADING = [x for x in range(1, COLUMNS + 1)]


def check_if_field_full(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                return True
    else:
        raise FieldFullError


def validate_column(column_idx):
    if not column_idx.isdigit():
        raise InvalidColumnInput
    else:
        if int(column_idx) < 1 or int(column_idx) > COLUMNS:
            raise InvalidColumnInput


def place_player_move(matrix, column_idx, player_id):
    for row_idx in range(ROWS - 1, - 1, -1):
        if matrix[row_idx][column_idx] != 0:
            continue
        else:
            # matrix[row_idx][column_idx] = player_id
            player_moved_bool = True
            current_row_idx = row_idx
            current_column_idx = column_idx
            return player_moved_bool, current_row_idx, current_column_idx
    else:
        raise ColumnFullError


def search_secondary_diagonal(matrix, row_idx, col_idx, player_idx):
    current_matrix = copy.deepcopy(matrix)
    result = 0

    if row_idx < 0 or col_idx < 0 or row_idx >= len(current_matrix) or col_idx >= len(current_matrix[0]):
        return 0
    if current_matrix[row_idx][col_idx] != player_idx:
        return 0

    current_matrix[row_idx][col_idx] = 'v'
    result += 1
    if result == 4:
        return result

    result += search_secondary_diagonal(current_matrix, row_idx - 1, col_idx + 1, player_idx)
    result += search_secondary_diagonal(current_matrix, row_idx + 1, col_idx - 1, player_idx)

    return result


def search_primary_diagonal(matrix, row_idx, col_idx, player_idx):
    current_matrix = copy.deepcopy(matrix)
    result = 0

    if row_idx < 0 or col_idx < 0 or row_idx >= len(current_matrix) or col_idx >= len(current_matrix[0]):
        return 0
    if current_matrix[row_idx][col_idx] != player_idx:
        return 0

    current_matrix[row_idx][col_idx] = 'v'
    result += 1
    if result == 4:
        return result

    result += search_primary_diagonal(current_matrix, row_idx - 1, col_idx - 1, player_idx)
    result += search_primary_diagonal(current_matrix, row_idx + 1, col_idx + 1, player_idx)

    return result


def search_horizontal(matrix, row_idx, col_idx, player_idx):
    current_matrix = copy.deepcopy(matrix)
    result = 0

    if row_idx < 0 or col_idx < 0 or row_idx >= len(current_matrix) or col_idx >= len(current_matrix[0]):
        return 0
    if current_matrix[row_idx][col_idx] != player_idx:
        return 0

    current_matrix[row_idx][col_idx] = 'v'
    result += 1
    if result == 4:
        return result

    result += search_horizontal(current_matrix, row_idx, col_idx - 1, player_idx)
    result += search_horizontal(current_matrix, row_idx, col_idx + 1, player_idx)

    return result


def search_vertical(matrix, row_idx, col_idx, player_idx):
    current_matrix = copy.deepcopy(matrix)
    result = 0

    if row_idx < 0 or col_idx < 0 or row_idx >= len(current_matrix) or col_idx >= len(current_matrix[0]):
        return 0
    if current_matrix[row_idx][col_idx] != player_idx:
        return 0

    current_matrix[row_idx][col_idx] = 'v'
    result += 1
    if result == 4:
        return result

    result += search_vertical(current_matrix, row_idx - 1, col_idx, player_idx)
    result += search_vertical(current_matrix, row_idx + 1, col_idx, player_idx)

    return result


def explore_if_four_connected(matrix, row_idx, column_idx, player_idx):
    player_won = False
    max_score = 0
    current_result_row = search_vertical(matrix, row_idx, column_idx, player_idx)
    if current_result_row > max_score:
        max_score = current_result_row
    current_result_column = search_horizontal(matrix, row_idx, column_idx, player_idx)
    if current_result_column > max_score:
        max_score = current_result_column
    current_result_primary_diagonal = search_primary_diagonal(matrix, row_idx, column_idx, player_idx)
    if current_result_primary_diagonal > max_score:
        max_score = current_result_primary_diagonal
    current_result_sec_diagonal = search_secondary_diagonal(matrix, row_idx, column_idx, player_idx)
    if current_result_sec_diagonal > max_score:
        max_score = current_result_sec_diagonal

    if max_score >= 4:
        player_won = True

    return player_won


field = [[0] * COLUMNS for _ in range(ROWS)]
players = deque()
player_counter = 0

while True:
    player_counter += 1
    player_name = input(f'Player {player_counter} input name: ')
    players.append((player_name, player_counter))
    print(f"Player {player_name} added")
    if player_counter == 2:
        print(f"{player_counter} players added! Enjoy the game!")
        break

while True:
    current_player = players.popleft()
    player, player_num = current_player
    while True:

        try:
            current_move = input(f'{player} enter column number (1-{COLUMNS}) ')
            validate_column(current_move)
        except InvalidColumnInput:
            print("Incorrect column number!")
            continue

        current_row = 0
        current_col = 0
        player_moved = False
        player_status = False

        column = int(current_move) - 1

        try:
            player_moved, current_row, current_col = place_player_move(field, column, player_num)
            field[current_row][current_col] = player_num
        except ColumnFullError:
            print("This column is full, Try another column!")
            continue

        if player_moved:
            players.append(current_player)
            break

    for line in field:
        print(line)
    print(COLUMNS_HEADING)

    player_status = explore_if_four_connected(field, current_row, current_col, player_num)

    if player_status:
        print(f"Congratulations! {player} won!")
        break

    try:
        check_if_field_full(field)
    except FieldFullError:
        print("No more space for moves. No winner! Game Over\nStart a new game")
