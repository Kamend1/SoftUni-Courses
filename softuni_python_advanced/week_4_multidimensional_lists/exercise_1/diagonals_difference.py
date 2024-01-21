size = int(input())
matrix = [[int(x) for x in input().split()] for rows in range(size)]

primary_diagonal = 0
secondary_diagonal = 0

for row in range(len(matrix)):
    col = row
    col_sec = size - row - 1
    primary_diagonal += matrix[row][col]
    secondary_diagonal += matrix[row][col_sec]

print(abs(primary_diagonal - secondary_diagonal))
