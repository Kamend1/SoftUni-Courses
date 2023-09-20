def dfs(key, row, column, matrix, visited):
    if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[0]):
        return
    if visited[row][column]:
        return
    if matrix[row][column] != key:
        return


    visited[row][column] = True
    dfs(key, row - 1, column, matrix, visited)
    dfs(key, row + 1, column, matrix, visited)
    dfs(key, row, column - 1, matrix, visited)
    dfs(key, row, column + 1, matrix, visited)


rows = int(input())
columns = int(input())
matrix = []
visited = []
areas = {}
total_areas = 0
for i in range(rows):
    matrix.append(list(input()))
    visited.append([False] * columns)

for row in range(rows):
    for column in range(columns):
        if visited[row][column]:
            continue
        key = matrix[row][column]
        dfs(key, row, column, matrix, visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1
        total_areas += 1
print(f'Areas: {total_areas}')
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")
