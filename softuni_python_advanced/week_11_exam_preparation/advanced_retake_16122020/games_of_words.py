initial_string = input()
size = int(input())

matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    line = list(input())
    matrix.append(line)

    if "P" in line:
        start_col = line.index("P")
        position = (row, start_col)

number_of_moves = int(input())
current_row, current_col = position

for _ in range(number_of_moves):
    direction = input()

    next_row, next_col = current_row + directions[direction][0], current_col +directions[direction][1]

    if 0 <= next_row < size and 0 <= next_col < size:
        if matrix[next_row][next_col] != '-':
            initial_string += matrix[next_row][next_col]
            matrix[next_row][next_col] = "P"
            matrix[current_row][current_col] = "-"
            current_row, current_col = next_row, next_col
        else:
            matrix[next_row][next_col] = "P"
            matrix[current_row][current_col] = "-"
            current_row, current_col = next_row, next_col
    else:
        if initial_string:
            initial_string = initial_string[0:-1]


print(initial_string)
for line in matrix:
    print(''.join(line))
