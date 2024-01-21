size = int(input())
matrix = [[int(x) for x in input().split(', ')] for rows in range(size)]

primary_diagonal_list = [matrix[row][row] for row in range(size)]
secondary_diagonal_list = [matrix[row][size - row - 1] for row in range(size)]


# for row in range(len(matrix)):
#     col = row
#     primary_diagonal_list.append(matrix[row][col])
#     primary_diagonal += matrix[row][col]
#     col = -row + len(matrix) - 1
#     secondary_diagonal_list.append(matrix[row][col])
#     secondary_diagonal += matrix[row][col]

# for row in range(len(matrix)):
#     col = -row + len(matrix) - 1
#     secondary_diagonal_list.append(matrix[row][col])
#     secondary_diagonal += matrix[row][col]

print(
    f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal_list)}. Sum: {sum(primary_diagonal_list)}"'\n'
    f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal_list)}. Sum: {sum(secondary_diagonal_list)}"
)
