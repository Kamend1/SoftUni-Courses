def find_all_paths(row, column, labyrinth, direction, path):
    if row < 0 or column < 0 or row >= len(labyrinth) or column >= len(labyrinth[0]):
        return
    if labyrinth[row][column] == "*":
        return
    if labyrinth[row][column] == "v":
        return

    path.append(direction)

    if labyrinth[row][column] == "e":
        print("".join(path))
    else:
        labyrinth[row][column] = "v"
        find_all_paths(row - 1, column, labyrinth, "U", path)
        find_all_paths(row + 1, column, labyrinth, "D", path)
        find_all_paths(row, column + 1, labyrinth, "R", path)
        find_all_paths(row, column - 1, labyrinth, "L", path)
        labyrinth[row][column] = "-"

    path.pop()


rows = int(input())
columns = int(input())

labyrinth = []

for i in range(rows):
    labyrinth.append(list(input()))

find_all_paths(0, 0, labyrinth, "", [])
