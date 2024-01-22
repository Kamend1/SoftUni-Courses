def find_bunny_location(matrix, size):
    start_row = 0
    start_col = 0
    for row_idx in range(size):
        for col_idx in range(size):
            if matrix[row_idx][col_idx] == 'B':
                start_row = row_idx
                start_col = col_idx
    return start_row, start_col


field_size = int(input())
field = [input().split() for _ in range(field_size)]

start_row_idx, start_col_idx = find_bunny_location(field, field_size)
best_route = []
most_eggs = -float('inf')
best_direction = ''

directions = {
    'left': [0, -1],
    'right': [0, +1],
    'up': [-1, 0],
    'down': [+1, 0],
}

for direction in directions.keys():
    bunny_row_idx, bunny_col_idx = start_row_idx, start_col_idx
    field[bunny_row_idx][bunny_col_idx] = 0
    current_eggs = 0
    visited = []

    while True:
        bunny_row_idx += directions[direction][0]
        bunny_col_idx += directions[direction][1]
        if 0 <= bunny_row_idx < field_size and 0 <= bunny_col_idx < field_size \
                and field[bunny_row_idx][bunny_col_idx] != 'X':
            visited.append([bunny_row_idx, bunny_col_idx])
            current_eggs += int(field[bunny_row_idx][bunny_col_idx])
        else:
            break

    if current_eggs >= most_eggs and visited:
        most_eggs = current_eggs
        best_direction = direction
        best_route = visited

print(best_direction)
for element in best_route:
    print(element)
print(most_eggs)
