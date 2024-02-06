rows, cols = (int(x) for x in input().split(', '))
matrix = []
total_items = 0

for row in range(rows):
    line = input().split()
    matrix.append(line)

    if "Y" in line:
        start_row = row
        start_col = line.index("Y")

    if 'C' in line:
        total_items += line.count("C")

    if 'G' in line:
        total_items += line.count("G")

    if 'D' in line:
        total_items += line.count("D")

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

row, col = start_row, start_col
collected_cookies = 0
collected_gifts = 0
collected_decorations = 0

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    direction, steps = command[0], int(command[1])

    for _ in range(steps):
        matrix[row][col] = 'x'
        row += directions[direction][0]
        if row < 0:
            row = rows - 1
        elif row == rows:
            row = 0

        col += directions[direction][1]
        if col < 0:
            col = cols - 1
        elif col == cols:
            col = 0

        if matrix[row][col] == 'C':
            matrix[row][col] = 'Y'
            collected_cookies += 1
            total_items -= 1
            if total_items == 0:
                print('Merry Christmas!')
                break
        elif matrix[row][col] == 'D':
            matrix[row][col] = 'Y'
            collected_decorations += 1
            total_items -= 1
            if total_items == 0:
                print('Merry Christmas!')
                break
        elif matrix[row][col] == 'G':
            matrix[row][col] = 'Y'
            collected_gifts += 1
            total_items -= 1
            if total_items == 0:
                print('Merry Christmas!')
                break

    matrix[row][col] = "Y"

    if total_items == 0:
        break

print(f"You've collected:\n"
      f" - {collected_decorations} Christmas decorations\n"
      f" - {collected_gifts} Gifts\n"
      f" - {collected_cookies} Cookies")
[print(' '.join(row)) for row in matrix]
