matrix = [[int(x) for x in input().split()] for rows in range(int(input()))]

primary_diagonal = 0
secondary_diagonal = 0

for row in range(len(matrix)):
    col = row
    primary_diagonal += matrix[row][col]

for row in range(len(matrix)):
    col = -row + len(matrix) - 1
    secondary_diagonal += matrix[row][col]

print(abs(primary_diagonal - secondary_diagonal))
