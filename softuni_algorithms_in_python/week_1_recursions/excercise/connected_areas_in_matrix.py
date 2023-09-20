class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size

def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'v'
    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result

rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
    matrix.append(list(input()))

area = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        area.append(Area(row, col, size))

print(f"Total areas found: {len(area)}")
for idx, area in enumerate(sorted(area, key=lambda a: a.size, reverse=True)):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')

area = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        area.append((row, col, size))

print(f"Total areas found: {len(area)}")
for idx, (row, col, size) in enumerate(sorted(area, key=lambda a: -a[2])):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')