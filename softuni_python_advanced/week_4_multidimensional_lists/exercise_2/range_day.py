def starting_position(matrix: list):
    row_idx = 0
    col_idx = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 'A':
                row_idx, col_idx = i, j
    return row_idx, col_idx


def count_targets(matrix):
    counter = 0
    for idx in range(5):
        for col_idx in range(5):
            if matrix[idx][col_idx] == 'x':
                counter += 1
    return counter


def shooter_move(row_idx, col_idx, matrix, command, steps):
    matrix[row_idx][col_idx] = '.'
    for _ in range(steps):
        row_idx += directions[command][0]
        col_idx += directions[command][1]

    if 0 <= row_idx < 5 and 0 <= col_idx < 5 and matrix[row_idx][col_idx] != 'x':
        matrix[row_idx][col_idx] = 'A'
    else:
        for _ in range(steps):
            row_idx -= directions[command][0]
            col_idx -= directions[command][1]
        matrix[row_idx][col_idx] = 'A'

    return row_idx, col_idx


def shoot(row_idx, col_idx, matrix, command, counter):
    row_idx += directions[command][0]
    col_idx += directions[command][1]
    while True:
        if row_idx < 0 or row_idx == 5 or col_idx < 0 or col_idx == 5:
            break
        if matrix[row_idx][col_idx] == 'x':
            counter -= 1
            matrix[row_idx][col_idx] = '.'
            targets_hit.append([row_idx, col_idx])
            break
        row_idx += directions[command][0]
        col_idx += directions[command][1]
    return counter


rows, cols = 5, 5
shooting_range = [[x for x in input().split()] for _ in range(rows)]
number_commands = int(input())
targets_hit = []

directions = {
    'left': [0, -1],
    'right': [0, +1],
    'up': [-1, 0],
    'down': [+1, 0],
}

current_row, current_col = starting_position(shooting_range)
number_of_targets = count_targets(shooting_range)

for _ in range(number_commands):
    if number_of_targets > 0:
        user_command = input().split()
    else:
        break
    if user_command[0] == 'move':
        direction, num_steps = user_command[1], int(user_command[2])
        current_row, current_col = shooter_move(current_row, current_col, shooting_range, direction, num_steps)
    elif user_command[0] == 'shoot':
        direction = user_command[1]
        number_of_targets = shoot(current_row, current_col, shooting_range, direction, number_of_targets)

if number_of_targets == 0:
    print(f'Training completed! All {len(targets_hit)} targets hit.')
else:
    print(f'Training not completed! {number_of_targets} targets left.')
for target in targets_hit:
    print(target)
