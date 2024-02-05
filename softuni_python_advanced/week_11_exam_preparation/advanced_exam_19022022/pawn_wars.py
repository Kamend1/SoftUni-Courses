rows, cols = 8, 8
board = []
board_titles = [["" for _ in range(cols)] for _ in range(rows)]
column_titles = "abcdefgh"

for row in range(rows, 0, -1):
    for col in range(len(column_titles)):
        board_titles[8 - row][col] = f"{column_titles[col]}{row}"

for row in range(rows):
    line = input().split()
    board.append(line)

    if 'w' in line:
        white_row = row
        white_col = line.index('w')

    if 'b' in line:
        black_row = row
        black_col = line.index('b')

while True:
    if white_col - 1 >= 0:
        if board[white_row - 1][white_col - 1] == 'b':
            print(f"Game over! White win, capture on {board_titles[white_row - 1][white_col - 1]}.")
            break

    if white_col + 1 < cols:
        if board[white_row - 1][white_col + 1] == 'b':
            print(f"Game over! White win, capture on {board_titles[white_row - 1][white_col + 1]}.")
            break

    white_row -= 1
    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {board_titles[white_row][white_col]}.")
        break
    else:
        board[white_row + 1][white_col] = '-'
        board[white_row][white_col] = 'w'

    if black_col - 1 >= 0:
        if board[black_row + 1][black_col - 1] == 'w':
            print(f"Game over! Black win, capture on {board_titles[black_row + 1][black_col - 1]}.")
            break

    if black_col + 1 < cols:
        if board[black_row + 1][black_col + 1] == 'w':
            print(f"Game over! Black win, capture on {board_titles[black_row + 1][black_col + 1]}.")
            break

    black_row += 1
    if black_row == rows - 1:
        print(f"Game over! Black pawn is promoted to a queen at {board_titles[black_row][black_col]}.")
        break
    else:
        board[black_row - 1][black_col] = '-'
        board[black_row][black_col] = 'b'
