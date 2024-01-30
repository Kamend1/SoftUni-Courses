size = int(input())
commands = [el for el in input().split(', ')]
field = []
collected_hazelnuts = 0

for row in range(size):
    line = [el for el in input()]
    field.append(line)

    if 's' in line:
        start_col = line.index('s')
        start_row = row

game_over = False

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

cur_row = start_row
cur_col = start_col

for command in commands:

    cur_row += directions[command][0]
    cur_col += directions[command][1]

    if cur_row < 0 or cur_row == size:
        print("The squirrel is out of the field.")
        game_over = True
        break

    if cur_col < 0 or cur_col == size:
        print("The squirrel is out of the field.")
        game_over = True
        break

    if field[cur_row][cur_col] == 't':
        print(f"Unfortunately, the squirrel stepped on a trap...")
        game_over = True
        break

    if field[cur_row][cur_col] == 'h':
        collected_hazelnuts += 1
        field[cur_row][cur_col] = '*'
        if collected_hazelnuts == 3:
            break

if not game_over:
    print("Good job! You have collected all hazelnuts!" if collected_hazelnuts == 3
      else "There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazelnuts}")
