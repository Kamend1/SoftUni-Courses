rows, cols = map(int, input().split(', '))
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

for col in range(cols):
    sum_col = 0
    for row in range(rows):
        sum_col += matrix[row][col]
    print(sum_col)
