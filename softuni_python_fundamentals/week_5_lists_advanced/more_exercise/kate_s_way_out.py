def find_all_paths(row, column, labyrinth, direction, path, all_paths):
    if row < 0 or column < 0 or row >= len(labyrinth) or column >= len(labyrinth[0]):
        return
    if labyrinth[row][column] == "#":
        return
    if labyrinth[row][column] == "v":
        return
    if labyrinth[row][column] == "k" and (row == 0 or row == rows - 1 or column == 0 or column == columns - 1):
        path_string = "S"
        all_paths.append(path_string)

    path.append(direction)

    if labyrinth[row][column] == "e":
        path_string = "".join(path)
        all_paths.append(path_string)
    else:
        labyrinth[row][column] = "v"
        find_all_paths(row - 1, column, labyrinth, "U", path, all_paths)
        find_all_paths(row + 1, column, labyrinth, "D", path, all_paths)
        find_all_paths(row, column + 1, labyrinth, "R", path, all_paths)
        find_all_paths(row, column - 1, labyrinth, "L", path, all_paths)
        labyrinth[row][column] = " "

    path.pop()
    if len(all_paths) == 0:
        return None

    result = len(all_paths)
    return result


rows = int(input())
labyrinth = []

for i in range(rows):
    labyrinth.append(list(input()))

columns = len(labyrinth[0])
starting_row = 0
starting_column = 0
all_paths_kate = []

for row in range(rows):
    for column in range(columns):
        if labyrinth[row][column] == "k":
            starting_row = row
            starting_column = column
        if (row == 0 or row == rows - 1 or column == 0 or column == columns - 1) and labyrinth[row][column] == " ":
            labyrinth[row][column] = "e"

find_all_paths(starting_row, starting_column, labyrinth, "S", [], all_paths_kate)
max_len = 0
for idx in range(len(all_paths_kate)):
    if len(all_paths_kate[idx]) > max_len:
        max_len = len(all_paths_kate[idx])

if find_all_paths(starting_row, starting_column, labyrinth, "S", [], all_paths_kate) == None:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {max_len} moves")
