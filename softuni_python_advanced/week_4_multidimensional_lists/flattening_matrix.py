rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

flattened_matrix = [num for sublist in matrix for num in sublist]
print(flattened_matrix)
