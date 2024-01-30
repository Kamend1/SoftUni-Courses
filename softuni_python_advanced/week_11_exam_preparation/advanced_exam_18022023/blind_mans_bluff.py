rows, cols = [int(x) for x in input().split()]
ground = []
counter_moves = 0
touched_opponents = 0

for row in range(rows):
    line = [el for el in input().split()]
    ground.append(line)

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
command = input()

while command != 'Finish':
    ground[current_row][current_col] = '-'
    current_row += directions[command][0]
    current_col += directions[command][1]

    if current_row < 0 or current_row == rows:
        current_row -= directions[command][0]
        current_col -= directions[command][1]
        ground[current_row][current_col] = 'B'

    if current_col < 0 or current_col == cols:
        current_row -= directions[command][0]
        current_col -= directions[command][1]
        ground[current_row][current_col] = 'B'

    if ground[current_row][current_col] == "O":
        current_row -= directions[command][0]
        current_col -= directions[command][1]
        ground[current_row][current_col] = 'B'

    if ground[current_row][current_col] == 'P':
        counter_moves += 1
        touched_opponents += 1
        ground[current_row][current_col] = 'B'
        if touched_opponents == 3:
            break

    if ground[current_row][current_col] == '-':
        ground[current_row][current_col] = 'B'
        counter_moves += 1

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {counter_moves}")
