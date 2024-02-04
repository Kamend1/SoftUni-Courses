import copy
from collections import deque
from random import randint


class FieldFullError(Exception):
    pass


class InvalidPlayerInput(Exception):
    pass


ROWS, COLUMNS = 3, 3
BOARD_MAPPING = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2),
}

directions = {
    'up': (-1, 0),
    'left': (0, -1),
    'upleft': (-1, -1),
    'upright': (-1, 1)
}


def check_if_field_full(matrix):
    if " " in matrix[0]:
        return True
    else:
        raise FieldFullError


def validate_play_input(play_input):
    if not play_input.isdigit():
        raise InvalidPlayerInput
    else:
        if int(play_input) < 1 or int(play_input) > 9:
            raise InvalidPlayerInput


def place_player_move(matrix, row_idx, column_idx):

    if matrix[row_idx][column_idx] != " ":
        raise FieldFullError
    else:
        player_moved_bool = True
        return player_moved_bool


def search_direction(matrix, row_idx, col_idx, player_idx, direction):
    current_matrix = copy.deepcopy(matrix)
    result = 0

    if row_idx < 0 or col_idx < 0 or row_idx >= len(current_matrix) or col_idx >= len(current_matrix[0]):
        return 0
    if current_matrix[row_idx][col_idx] != player_idx:
        return 0

    current_matrix[row_idx][col_idx] = 'v'
    result += 1
    if result == 3:
        return result

    coords = directions[direction]

    result += search_direction(current_matrix, row_idx + coords[0], col_idx + coords[1], player_idx, direction)
    result += search_direction(current_matrix, row_idx - coords[0], col_idx - coords[1], player_idx, direction)

    return result


def explore_if_three_connected(matrix, row_idx, column_idx, player_idx):
    player_won = False
    max_score = 0
    for direction in directions.keys():
        max_score = 0
        current_result = search_direction(matrix, row_idx, column_idx, player_idx, direction)
        if current_result > max_score:
            max_score = current_result
        if max_score >= 3:
            player_won = True

    return player_won


field = [[" "] * COLUMNS for _ in range(ROWS)]
players = deque()
player_counter = 0

while True:
    player_counter += 1
    player_name = input(f'Player {player_counter} input name: ')
    players.append([player_name, player_counter])
    print(f"Player {player_name} added")
    if player_counter == 2:
        print(f"{player_counter} players added! Enjoy the game!")
        turn = randint(1, 2)
        if turn == 1:
            players[0][1] = 'X'
            players[1][1] = 'O'
            print(f"{players[0][0]} starts first and plays with {players[0][1]}\n"
                  f"{players[1][0]} starts second and plays with {players[1][1]}")
        elif turn == 2:
            players[1][1] = 'X'
            players[0][1] = 'O'
            print(f"{players[1][0]} starts first and plays with {players[1][1]}\n"
                  f"{players[0][0]} starts second and plays with {players[0][1]}")
            player = players.popleft()
            players.append(player)
        print("This is the numeration of the fields on the board:")
        print("| 1 | 2 | 3 |")
        print("| 4 | 5 | 6 |")
        print("| 7 | 8 | 9 |")
        break

while True:
    current_player = players.popleft()
    player, player_sign = current_player
    while True:

        try:
            current_move = input(f'{player} enter field number (1-{COLUMNS * ROWS}) ')
            validate_play_input(current_move)
        except InvalidPlayerInput:
            print("Incorrect field number!")
            continue

        current_row, current_col = BOARD_MAPPING.get(current_move)
        player_moved = False
        player_status = False

        try:
            player_moved = place_player_move(field, current_row, current_col)
            field[current_row][current_col] = player_sign
        except FieldFullError:
            print("This field is full, Try another!")
            continue

        if player_moved:
            players.append(current_player)
            break

    for line in field:
        print(f"| {line[0]} | {line[1]} | {line[2]} |")

    player_status = explore_if_three_connected(field, current_row, current_col, player_sign)

    if player_status:
        print(f"Congratulations! {player} won!")
        break

    try:
        check_if_field_full(field)
    except FieldFullError:
        print("No more space for moves. No winner! Game Over\nStart a new game")
        exit(0)
