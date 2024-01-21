matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

command = input()

while command != "END":
    operation, row, col, value = command.split()
    if operation == "Add" and 0 <= int(row) < len(matrix) and 0 <= int(col) < len(matrix[int(row)]):
        matrix[int(row)][int(col)] += int(value)
    elif operation == "Subtract" and 0 <= int(row) < len(matrix) and 0 <= int(col) < len(matrix[int(row)]):
        matrix[int(row)][int(col)] -= int(value)
    else:
        print("Invalid coordinates")
    command = input()

for list in matrix:
    print(*list)
