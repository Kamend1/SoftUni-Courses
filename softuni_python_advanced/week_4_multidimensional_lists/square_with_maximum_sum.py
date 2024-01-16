from sys import maxsize
rows, cols = map(int, input().split(', '))
matrix = []
square_max_matrix = [[0 * j for j in range(2)] for i in range(2)]
max_square_matrix_sum = -maxsize

for _ in range(rows):
    matrix.append(list(map(int, input().split(', '))))

for row in range(rows):
    for col in range(cols):
        current_matrix = [[0 * j for j in range(2)] for i in range(2)]
        if row + 1 < rows and col + 1 < cols:
            current_matrix[0][0] = matrix[row][col]
            current_matrix[0][1] = matrix[row][col + 1]
            current_matrix[1][0] = matrix[row + 1][col]
            current_matrix[1][1] = matrix[row + 1][col + 1]
            current_sum = sum(sum(list) for list in current_matrix)
            if current_sum > max_square_matrix_sum:
                max_square_matrix_sum = current_sum
                square_max_matrix = current_matrix
for list in square_max_matrix:
    print(*list)
print(max_square_matrix_sum)
