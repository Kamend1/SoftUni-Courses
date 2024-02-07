ROWS, COLS = 6, 6
matrix = [input().split() for _ in range(ROWS)]
points = 0

for _ in range(3):
    coordinates = eval(input())
    row, col = int(coordinates[0]), int(coordinates[1])

    if 0 <= row < ROWS and 0 <= col < COLS:
        if matrix[row][col] == 'B':
            matrix[row][col] = 0
            for row in range(ROWS):
                points += int(matrix[row][col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
