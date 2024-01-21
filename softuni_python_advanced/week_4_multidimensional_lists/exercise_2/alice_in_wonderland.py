size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

number_tea_bags = 0

for row_idx in range(size):
    for col_idx in range(size):
        if matrix[row_idx][col_idx] == 'A':
            start_row, start_col = row_idx, col_idx

directions = {
    'left': [0, -1],
    'right': [0, +1],
    'up': [-1, 0],
    'down': [+1, 0],
}

current_row, current_col = start_row, start_col

while True:
    matrix[current_row][current_col] = '*'
    direction = input()

    current_row, current_col = current_row + directions[direction][0], current_col + directions[direction][1]
    if 0 <= current_row < size and 0 <= current_col < size:
        if matrix[current_row][current_col] == '.':
            matrix[current_row][current_col] = '*'
            continue
        elif matrix[current_row][current_col] == 'R':
            matrix[current_row][current_col] = '*'
            break
        elif matrix[current_row][current_col] == '*':
            continue
        else:
            number_tea_bags += matrix[current_row][current_col]
            matrix[current_row][current_col] = '*'
            if number_tea_bags >= 10:
                break
    else:
        break

if number_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
