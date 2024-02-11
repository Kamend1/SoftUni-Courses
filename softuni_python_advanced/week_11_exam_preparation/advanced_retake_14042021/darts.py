player_1, player_2 = input().split(", ")
rows, cols = 7, 7
board = [input().split() for _ in range(rows)]

sum_rows = {}
sum_cols = {}

for row in range(rows):
    sum_row = 0
    for element in board[row]:
        if element not in ['D', 'T', 'B']:
            sum_row += int(element)
    sum_rows[row] = sum_rows.get(row, 0) + sum_row

for col in range(cols):
    sum_col = 0
    for row in range(rows):
        if board[row][col] not in ['D', 'T', 'B']:
            sum_col += int(board[row][col])
    sum_cols[col] = sum_cols.get(col, 0) + sum_col

player_1_points = 501
player_2_points = 501
player_1_throws = 0
player_2_throws = 0
turns = 0

while True:
    turns += 1
    row, col = eval(input())

    if row < 0 or row >= rows or col < 0 or col >= cols:
        if turns % 2 != 0:
            player_1_throws += 1
        else:
            player_2_throws += 1
        continue

    if turns % 2 != 0:
        player_1_throws += 1
        if board[row][col] == "D":
            current_result = sum_rows[row] + sum_cols[col]
            player_1_points -= 2 * current_result
        elif board[row][col] == "T":
            current_result = sum_rows[row] + sum_cols[col]
            player_1_points -= 3 * current_result
        elif board[row][col] == "B":
            print(f"{player_1} won the game with {player_1_throws} throws!")
            break
        else:
            player_1_points -= int(board[row][col])

        if player_1_points <= 0:
            print(f"{player_1} won the game with {player_1_throws} throws!")
            break

    elif turns % 2 == 0:
        player_2_throws += 1
        if board[row][col] == "D":
            current_result = sum_rows[row] + sum_cols[col]
            player_2_points -= 2 * current_result
        elif board[row][col] == "T":
            current_result = sum_rows[row] + sum_cols[col]
            player_2_points -= 3 * current_result
        elif board[row][col] == "B":
            print(f"{player_2} won the game with {player_2_throws} throws!")
            break
        else:
            player_2_points -= int(board[row][col])

        if player_2_points <= 0:
            print(f"{player_2} won the game with {player_2_throws} throws!")
            break
