from collections import deque

rows, cols = 6, 6
matrix = []
discovered_deposits = set()

directions = {
    'up': [-1, 0],
    'down': [+1, 0],
    'left': [0, -1],
    'right': [0, +1],
}

for index in range(rows):
    line = input().split()
    matrix.append(line)
    if 'E' in line:
        start_row = index
        start_col = line.index('E')

commands = deque(input().split(', '))

row, col = start_row, start_col

while True:
    matrix[row][col] = '-'
    current_command = commands.popleft()
    row += directions[current_command][0]
    col += directions[current_command][1]

    if row < 0:
        row = rows - 1

    if row == rows:
        row = 0

    if col < 0:
        col = cols - 1

    if col == cols:
        col = 0

    if matrix[row][col] == 'W':
        discovered_deposits.add('W')
        print(f'Water deposit found at ({row}, {col})')
    elif matrix[row][col] == 'M':
        discovered_deposits.add('M')
        print(f'Metal deposit found at ({row}, {col})')
    elif matrix[row][col] == 'C':
        discovered_deposits.add('C')
        print(f'Concrete deposit found at ({row}, {col})')
    elif matrix[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break

    if not commands:
        break

if len(discovered_deposits) == 3:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
