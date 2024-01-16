rows, cols = (int(x) for x in input().split())
matrix = [["" for _ in range(cols)] for _ in range(rows)]
expression = input()

number_of_cells = rows * cols
full_lengths = number_of_cells // len(expression)
remainder = number_of_cells - full_lengths * len(expression)
total_string = expression * full_lengths + expression[:remainder]
index = 0
row = 0
col = 0

for _ in range(number_of_cells):
    matrix[row][col] = total_string[index]
    index += 1
    if row % 2 == 0:
        col += 1
        if col == cols:
            col -= 1
            row += 1
    else:
        col -= 1
        if col < 0:
            row += 1
            col = 0

for list in matrix:
    print(''.join(list))
