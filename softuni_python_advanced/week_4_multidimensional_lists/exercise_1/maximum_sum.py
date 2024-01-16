from sys import maxsize

rows, cols = (int(x) for x in input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = -maxsize
max_sum_matrix = [[0 for _ in range(3)] for _ in range(3)]

for row in range(rows):
    for col in range(cols):
        current_matrix = [[0 for _ in range(3)] for _ in range(3)]
        current_sum = 0
        if row + 2 < rows and col + 2 < cols:
            current_matrix[0][0] = matrix[row][col]
            current_matrix[0][1] = matrix[row][col + 1]
            current_matrix[0][2] = matrix[row][col + 2]
            current_matrix[1][0] = matrix[row + 1][col]
            current_matrix[1][1] = matrix[row + 1][col + 1]
            current_matrix[1][2] = matrix[row + 1][col + 2]
            current_matrix[2][0] = matrix[row + 2][col]
            current_matrix[2][1] = matrix[row + 2][col + 1]
            current_matrix[2][2] = matrix[row + 2][col + 2]
            current_sum += sum(sum(list) for list in current_matrix)
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_matrix = current_matrix

print(f"Sum = {max_sum}")
for list in max_sum_matrix:
    print(*list)
