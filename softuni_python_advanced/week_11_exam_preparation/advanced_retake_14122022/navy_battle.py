size = int(input())
field = []
number_hits = 0
ships_sunk = 0

for row in range(size):
    line = list(input())
    field.append(line)
    if 'S' in line:
        index = line.index('S')
        start_row = row
        start_col = index
        field[start_row][start_col] = '-'

directions = {
    'up': (- 1, 0),
    'down': (+ 1, 0),
    'left': (0, - 1),
    'right': (0, + 1),
}

row = start_row
col = start_col

while True:
    command = input()
    field[row][col] = '-'

    row += directions[command][0]
    col += directions[command][1]

    if field[row][col] == '*':
        number_hits += 1
        field[row][col] = 'S'
        if number_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break

    if field[row][col] == '-':
        field[row][col] = 'S'

    if field[row][col] == 'C':
        field[row][col] = 'S'
        ships_sunk += 1
        if ships_sunk == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break


for line in field:
    print(''.join(line))
