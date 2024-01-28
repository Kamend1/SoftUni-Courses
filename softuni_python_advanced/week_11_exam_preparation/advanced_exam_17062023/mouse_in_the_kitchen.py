rows, cols = (int(x) for x in input().split(','))
field = []
cheese_counter = 0

for row in range(rows):
    line = [el for el in input()]
    field.append(line)

    if 'M' in line:
        start_row = row
        start_col = line.index('M')

    if 'C' in line:
        result = line.count('C')
        cheese_counter += result

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

current_row = start_row
current_col = start_col
command = input()

while True:
    field[current_row][current_col] = '*'
    current_row += directions[command][0]
    current_col += directions[command][1]

    if current_row < 0 or current_row == rows:
        current_row -= directions[command][0]
        current_col -= directions[command][1]
        field[current_row][current_col] = 'M'
        print("No more cheese for tonight!")
        break

    if current_col < 0 or current_col == cols:
        current_row -= directions[command][0]
        current_col -= directions[command][1]
        field[current_row][current_col] = 'M'
        print("No more cheese for tonight!")
        break

    if field[current_row][current_col] == '@':
        current_row -= directions[command][0]
        current_col -= directions[command][1]
        field[current_row][current_col] = 'M'

    if field[current_row][current_col] == 'C':
        field[current_row][current_col] = 'M'
        cheese_counter -= 1
        if cheese_counter == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    if field[current_row][current_col] == 'T':
        field[current_row][current_col] = 'M'
        print("Mouse is trapped!")
        break

    if field[current_row][current_col] == '*':
        field[current_row][current_col] = 'M'

    command = input()

    if command == 'danger':
        print("Mouse will come back later!")
        break

[print(''.join(line)) for line in field]
