matrix = [[int(x) for x in input().split(', ')] for rows in range(int(input()))]

primary_diagonal_list = []
primary_diagonal = 0
secondary_diagonal_list = []
secondary_diagonal = 0

for row in range(len(matrix)):
    col = row
    primary_diagonal_list.append(matrix[row][col])
    primary_diagonal += matrix[row][col]

for row in range(len(matrix)):
    col = -row + len(matrix) - 1
    secondary_diagonal_list.append(matrix[row][col])
    secondary_diagonal += matrix[row][col]

print(
    f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal_list)}. Sum: {primary_diagonal}"'\n'
    f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal_list)}. Sum: {secondary_diagonal}"
)
