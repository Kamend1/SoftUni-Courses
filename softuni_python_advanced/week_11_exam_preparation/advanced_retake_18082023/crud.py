def create(direction, value, nested_list, row, col):
    row += directions[direction][0]
    col += directions[direction][1]
    if nested_list[row][col] == '.':
        nested_list[row][col] = value
    return nested_list, row, col


def update(direction, value, nested_list, row, col):
    row += directions[direction][0]
    col += directions[direction][1]
    if nested_list[row][col] != '.':
        nested_list[row][col] = value
    return nested_list, row, col


def delete(direction, nested_list, row, col):
    row += directions[direction][0]
    col += directions[direction][1]
    if nested_list[row][col] != '.':
        nested_list[row][col] = '.'
    return nested_list, row, col


def read(direction, nested_list, row, col):
    row += directions[direction][0]
    col += directions[direction][1]
    if nested_list[row][col] != '.':
        print(nested_list[row][col])
    return nested_list, row, col

rows, cols = 6, 6
matrix = [[x for x in input().split()] for _ in range(rows)]

first_position = input().strip('()')
current_row, current_col = (int(x) for x in first_position.split(', '))


directions = {
    'up': (- 1, 0),
    'down': (+ 1, 0),
    'left': (0, - 1),
    'right': (0, + 1),
}

commands = input().split(', ')

while commands[0] != 'Stop':

    if commands[0] == 'Create':
        matrix, current_row, current_col = create(commands[1], commands[2], matrix, current_row, current_col)
    elif commands[0] == 'Update':
        matrix, current_row, current_col = update(commands[1], commands[2], matrix, current_row, current_col)
    elif commands[0] == 'Read':
        matrix, current_row, current_col = read(commands[1], matrix, current_row, current_col)
    elif commands[0] == 'Delete':
        matrix, current_row, current_col = delete(commands[1], matrix, current_row, current_col)

    commands = input().split(', ')

for line in matrix:
    print(' '.join(line))
