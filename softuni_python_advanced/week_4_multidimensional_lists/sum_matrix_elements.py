rows, columns = map(int, input().split(', '))
matrix = []
sum_matrix = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
    sum_matrix += sum(matrix[row])

print(sum_matrix, matrix, sep='\n')
