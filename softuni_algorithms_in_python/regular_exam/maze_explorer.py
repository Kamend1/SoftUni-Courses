def find_all_paths(row, column, labyrinth, direction, path, best_path):
    if row < 0 or column < 0 or row >= len(labyrinth) or column >= len(labyrinth[0]):
        return
    if labyrinth[row][column] == "#":
        return
    if labyrinth[row][column] == "v":
        return

    path.append(direction)

    if labyrinth[row][column] == "E":
        if len(path) < best_path[0]:
            best_path[0] = len(path)

    else:
        labyrinth[row][column] = "v"
        find_all_paths(row - 1, column, labyrinth, "U", path, best_path)
        find_all_paths(row + 1, column, labyrinth, "D", path, best_path)
        find_all_paths(row, column + 1, labyrinth, "R", path, best_path)
        find_all_paths(row, column - 1, labyrinth, "L", path, best_path)
        labyrinth[row][column] = "."

    path.pop()

rows = int(input())
columns = rows
best_path = [float('inf')]
labyrinth = []

for i in range(rows):
    labyrinth.append(list(input()))

find_all_paths(0, 0, labyrinth, "", [], best_path)
print(best_path[0] - 1)
