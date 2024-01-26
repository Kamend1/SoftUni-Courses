size = int(input())
field = []
quota = 20
total_catch = 0
ship_sunk = False

for idx in range(size):
    line = [el for el in input()]
    field.append(line)

    if 'S' in line:
        col = line.index('S')
        row = idx
        field[row][col] = '-'

directions = {
    'up': [-1, 0],
    'down': [+1, 0],
    'left': [0, -1],
    'right': [0, +1],
}

command = input()

while command != 'collect the nets':
    field[row][col] = '-'

    row += directions[command][0]
    if row == size:
        row = 0
    elif row < 0:
        row = size - 1

    col += directions[command][1]
    if col == size:
        col = 0
    elif col < 0:
        col = size - 1

    if field[row][col] == 'W':
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
        ship_sunk = True
        break

    if field[row][col] != '-':
        quota -= int(field[row][col])
        total_catch += int(field[row][col])
        field[row][col] = 'S'

    if field[row][col] == '-':
        field[row][col] = 'S'

    command = input()


if not ship_sunk:
    if quota > 0:
        print(f"You didn't catch enough fish and didn't reach the quota! "
              f"You need {quota} tons of fish more.")
    else:
        print("Success! You managed to reach the quota!")

    if total_catch > 0:
        print(f"Amount of fish caught: {total_catch} tons.")

    for line in field:
        print(''.join(line))
