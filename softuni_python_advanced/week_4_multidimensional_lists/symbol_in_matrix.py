rows = int(input())
cols = rows
matrix = []

for row in range(rows):
    matrix.append([char for char in input()])

searched_symbol = input()
found = False
location = ()

for row in range(rows):
    if found:
        break
    for col in range(cols):
        if matrix[row][col] == searched_symbol:
            location = (row, col)
            found = True
            print(location)

if not found:
    print(f"{searched_symbol} does not occur in the matrix")
