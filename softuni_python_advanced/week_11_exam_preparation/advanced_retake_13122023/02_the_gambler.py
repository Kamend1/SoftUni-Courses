size = int(input())
field = []

for row in range(size):
    line = list(input())
    field.append(line)
    if 'G' in line:
        g_idx = line.index('G')
        g_pos_row = row
        g_pos_col = g_idx
        field[row][g_idx] = '-'

total_amount = 100

directions = {
    'up': (- 1, 0),
    'down': (+ 1, 0),
    'left': (0, - 1),
    'right': (0, + 1),
}

while True:
    command = input()

    if command == 'end':
        print(f"End of the game. Total amount: {total_amount}$")
        field[g_pos_row][g_pos_col] = 'G'
        break

    g_pos_row += directions[command][0]
    g_pos_col += directions[command][1]

    if 0 <= g_pos_row < size and 0 <= g_pos_col < size:
        if field[g_pos_row][g_pos_col] == 'J':
            total_amount += 100000
            field[g_pos_row][g_pos_col] = 'G'
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {total_amount}$")
            break
        elif field[g_pos_row][g_pos_col] == 'P':
            total_amount -= 200
            field[g_pos_row][g_pos_col] = '-'
            if total_amount <= 0:
                print("Game over! You lost everything!")
                break
        elif field[g_pos_row][g_pos_col] == 'W':
            total_amount += 100
            field[g_pos_row][g_pos_col] = '-'
    else:
        g_pos_row -= directions[command][0]
        g_pos_col -= directions[command][1]
        field[g_pos_row][g_pos_col] = 'G'
        print(f"End of the game. Total amount: {total_amount}$")
        break

if total_amount > 0:
    [print(''.join(x for x in row)) for row in field]
