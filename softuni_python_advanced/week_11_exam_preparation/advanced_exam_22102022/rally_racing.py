size = int(input())
racing_number = input()
track = []
kilometers_passed = 0
tunnels = []
finished = False
current_row = 0
current_col = 0

for idx in range(size):
    line = input().split()
    track.append(line)
    for col_idx, cell in enumerate(line):
        if cell == 'T':
            tunnels.append((idx, col_idx))

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

command = input()

while command != "End":
    current_row += directions[command][0]
    current_col += directions[command][1]

    if track[current_row][current_col] == ".":
        kilometers_passed += 10


    if track[current_row][current_col] == "T":
        track[current_row][current_col] = "."
        tunnels.remove((current_row, current_col))
        current_row, current_col = tunnels.pop()
        track[current_row][current_col] = "."
        kilometers_passed += 30

    if track[current_row][current_col] == "F":
        finished = True
        kilometers_passed += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

    command = input()

if not finished:
    print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {kilometers_passed} km.")

track[current_row][current_col] = "C"
for line in track:
    print(''.join(line))
