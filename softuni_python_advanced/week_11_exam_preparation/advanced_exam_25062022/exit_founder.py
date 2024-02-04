from collections import deque

players = deque(input().split(", "))
rows, cols = 6, 6
matrix = []



for _ in range(rows):
    line = [x for x in input().split()]
    matrix.append(line)

while True:
    coords = input()
    current_row = int(coords[1])
    current_col = int(coords[4])
    current_player = players.popleft()
    if 'rest' in current_player:
        current_player = current_player.replace('rest', '')
        players.append(current_player)
        continue

    if matrix[current_row][current_col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    if matrix[current_row][current_col] == 'T':
        second_player = players.pop()
        print(f"{current_player} is out of the game! The winner is {second_player}.")
        break


    if matrix[current_row][current_col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        current_player += 'rest'

    players.append(current_player)
