from collections import deque

def search_direction(matrix, row_idx, col_idx, player_idx, direction):
    result = 1
    cur_row = int(row_idx)
    cur_col = int(col_idx)
    while True:
        cur_row += direction[0]
        cur_col += direction[1]

        if cur_row < 0 or cur_col < 0 or cur_row >= len(matrix) or cur_col >= len(matrix[0]):
            break

        if matrix[cur_row][cur_col] != player_idx:
            break

        result += 1

        if result == 4:
            break

    return result


def explore_if_four_connected(matrix, row_idx, column_idx, player_idx):
    player_won = False
    for dir in directions.values():
        current_result = search_direction(matrix, row_idx, column_idx, player_idx, dir)
        if current_result == 4:
            player_won = True

    return player_won


field = [[0] * 7 for _ in range(6)]
players = deque()
player_counter = 0

while True:
    answer = input('Do you want to add a player - yes or no: ')
    if answer == 'yes':
        player_counter += 1
        player_name = input('Player name: ')
        players.append((player_name, player_counter))
        print(f"Player {player_name} added")
        if player_counter == 5:
            print(f"Max {player_counter} players added! Enjoy the game!")
    elif answer == 'no':
        if player_counter >= 2:
            print("OK, let's start the game!")
            break
        else:
            print("You need minimum two players!")
    else:
        print("You must enter yes or no!")

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
    'up_left': (-1, -1),
    'up_right': (-1, +1),
    'down_left': (+1, -1),
    'down_right': (+1, +1),
}

while True:
    current_player = players.popleft()
    player, player_num = current_player
    while True:
        current_move = input(f'{player} enter column number (1-7) ')
        current_row = 0
        current_col = 0
        player_moved = False
        player_status = False
        if 1 <= int(current_move) <= 7:
            column = int(current_move) - 1
            for row in range(len(field) - 1, - 1, -1):
                if row != 0:
                    if field[row][column] != 0:
                        continue
                    else:
                        field[row][column] = player_num
                        player_moved = True
                        current_row = row
                        current_column = column
                        break
                else:
                    if field[row][column] != 0:
                        print("This column is full")
                    else:
                        field[row][column] = player_num
                        player_moved = True
                        current_row = row
                        current_column = column
                        break
        else:
            print("Incorrect column")

        if player_moved:
            players.append(current_player)
            break

    for line in field:
        print(line)

    player_status = explore_if_four_connected(field, current_row, current_column, player_num)
    if player_status:
        print(f"Congratulations! {player} won!")
        break

    if player_status:
        break
