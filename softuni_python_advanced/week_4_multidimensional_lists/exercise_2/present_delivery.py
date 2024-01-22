def starting_position(matrix: list, length):
    row_idx = 0
    col_idx = 0
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == 'S':
                row_idx, col_idx = i, j
    return row_idx, col_idx


def count_nice_kids(matrix, length):
    counter = 0
    for idx in range(length):
        for col_idx in range(length):
            if matrix[idx][col_idx] == 'V':
                counter += 1
    return counter


def santa_move(matrix, action, row, col, presents, kids, kids_presents):
    matrix[row][col] = '-'
    row += directions[action][0]
    col += directions[action][1]

    if matrix[row][col] == 'V':
        kids -= 1
        presents -= 1
        kids_presents += 1
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'X':
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'C':
        matrix[row][col] = 'S'
        for key in directions.keys():
            current_r = 0
            current_c = 0
            current_r = row + directions[key][0]
            current_c = col + directions[key][1]

            if matrix[current_r][current_c] == 'X':
                matrix[current_r][current_c] = '-'
                presents -= 1
            elif matrix[current_r][current_c] == 'V':
                matrix[current_r][current_c] = '-'
                presents -= 1
                kids -= 1
                kids_presents += 1

            if presents == 0:
                break

    return matrix, row, col, presents, kids, kids_presents


number_presents = int(input())
size = int(input())
town = [[el for el in input().split()] for _ in range(size)]

directions = {
    'left': [0, -1],
    'right': [0, +1],
    'up': [-1, 0],
    'down': [+1, 0],
}

santa_row, santa_col = starting_position(town, size)
number_nice_kids = count_nice_kids(town, size)
nice_kids_with_presents = 0

while number_presents > 0:
    command = input()
    if command == 'Christmas morning':
        break
    town, santa_row, santa_col, number_presents, number_nice_kids, nice_kids_with_presents = \
        santa_move(town, command, santa_row, santa_col, number_presents, number_nice_kids, nice_kids_with_presents)
    if number_presents == 0 and number_nice_kids > 0:
        print("Santa ran out of presents!")
        break

[print(*row) for row in town]
if number_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {number_nice_kids} nice kid/s.")
