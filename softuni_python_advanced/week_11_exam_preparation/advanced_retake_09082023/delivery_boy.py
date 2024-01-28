rows, cols = (int(x) for x in input().split())
field = []

for row in range(rows):
    line = [el for el in input()]
    field.append(line)

    if 'B' in line:
        start_row = row
        start_col = line.index('B')

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

current_row = start_row
current_col = start_col

while True:
    command = input()
    current_row += directions[command][0]
    current_col += directions[command][1]

    if current_row < 0 or current_row == rows:
        print("The delivery is late. Order is canceled.")
        field[start_row][start_col] = " "
        break

    if current_col < 0 or current_col == cols:
        print("The delivery is late. Order is canceled.")
        field[start_row][start_col] = " "
        break

    if field[current_row][current_col] == '*':
        current_row -= directions[command][0]
        current_col -= directions[command][1]

    if field[current_row][current_col] == '-':
        field[current_row][current_col] = '.'

    if field[current_row][current_col] == 'P':
        field[current_row][current_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")

    if field[current_row][current_col] == 'A':
        field[current_row][current_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

for line in field:
    print(''.join(line))
