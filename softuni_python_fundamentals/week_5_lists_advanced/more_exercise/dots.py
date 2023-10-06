def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '.':
        return 0

    matrix[row][col] = 'v'
    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result


number_of_rows = int(input())
matrix = []
size_connected_areas = []

for row in range(number_of_rows):
    matrix.append(list(input().split()))

for row in range(number_of_rows):
    for col in range(len(matrix[0])):
        current_size = explore_area(row, col, matrix)
        if current_size == 0:
            continue
        size_connected_areas.append(current_size)

if len(size_connected_areas) != 0:
    print(max(size_connected_areas))
else:
    print(0)
