size = int(input())

sky = []
armor = 300
start_pos = (0, 0)
enemies = 4

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

for row_idx in range(size):
    line = list(input())
    sky.append(line)

    if 'J' in line:
        start_pos = (row_idx, line.index('J'))

row, col = start_pos

while True:
    sky[row][col] = '-'

    direction = input()

    row += directions[direction][0]
    col += directions[direction][1]

    if sky[row][col] == 'R':
        sky[row][col] = 'J'
        armor = 300

    if sky[row][col] == '-':
        sky[row][col] = 'J'

    if sky[row][col] == 'E':
        sky[row][col] = 'J'
        enemies -= 1
        if enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -= 100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
                break

for line in sky:
    print(''.join(line))
