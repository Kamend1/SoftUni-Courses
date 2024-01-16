rows = int(input())
cols = rows
matrix = []
sum_diagonal = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

for row in range(rows):
    col = row
    sum_diagonal += matrix[row][col]

print(sum_diagonal)
