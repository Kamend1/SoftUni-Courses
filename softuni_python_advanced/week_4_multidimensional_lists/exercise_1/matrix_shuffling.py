rows, cols = (int(x) for x in input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input().split()
while command[0] != 'END':
    if len(command) == 5 and 0 <= int(command[1]) < rows and 0 <= int(command[2]) < cols \
            and 0 <= int(command[3]) < rows and 0 <= int(command[4]) < cols:
        first_value = matrix[int(command[1])][int(command[2])]
        second_value = matrix[int(command[3])][int(command[4])]
        matrix[int(command[3])][int(command[4])] = first_value
        matrix[int(command[1])][int(command[2])] = second_value
        for list in matrix:
            print(*list)
    else:
        print('Invalid input!')
    command = input().split()
