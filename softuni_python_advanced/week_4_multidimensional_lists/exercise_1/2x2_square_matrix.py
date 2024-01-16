rows, cols = (int(x) for x in input().split())
matrix = [[char for char in input().split()] for _ in range(rows)]
number_square_matrices = 0

for row in range(rows):
    for col in range(cols):
        if row + 1 < rows and col + 1 < cols:
            symbol = matrix[row][col]
            if matrix[row][col + 1] == symbol and matrix[row + 1][col] == symbol and matrix[row + 1][col + 1] == symbol:
                number_square_matrices += 1

print(number_square_matrices)
