from collections import deque

size = int(input())
commands = deque(input().split())
field = [input().split() for _ in range(size)]
amount_coal = 0

for i in range(size):
    for j in range(size):
        if field[i][j] == 'c':
            amount_coal += 1
        elif field[i][j] == 's':
            start_row = i
            start_col = j

while commands:
    current_command = commands.popleft()
    if current_command == 'left':
        start_col -= 1
        if 0 <= start_row < size and 0 <= start_col < size:
            if field[start_row][start_col] == 'c':
                amount_coal -= 1
                field[start_row][start_col] = '*'
                if amount_coal == 0:
                    print(f"You collected all coal! ({start_row}, {start_col})")
                    break
            elif field[start_row][start_col] == 'e':
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_col += 1
    elif current_command == 'right':
        start_col += 1
        if 0 <= start_row < size and 0 <= start_col < size:
            if field[start_row][start_col] == 'c':
                amount_coal -= 1
                field[start_row][start_col] = '*'
                if amount_coal == 0:
                    print(f"You collected all coal! ({start_row}, {start_col})")
                    break
            elif field[start_row][start_col] == 'e':
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_col -= 1
    elif current_command == 'up':
        start_row -= 1
        if 0 <= start_row < size and 0 <= start_col < size:
            if field[start_row][start_col] == 'c':
                amount_coal -= 1
                field[start_row][start_col] = '*'
                if amount_coal == 0:
                    print(f"You collected all coal! ({start_row}, {start_col})")
                    break
            elif field[start_row][start_col] == 'e':
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_row += 1
    elif current_command == 'down':
        start_row += 1
        if 0 <= start_row < size and 0 <= start_col < size:
            if field[start_row][start_col] == 'c':
                amount_coal -= 1
                field[start_row][start_col] = '*'
                if amount_coal == 0:
                    print(f"You collected all coal! ({start_row}, {start_col})")
                    break
            elif field[start_row][start_col] == 'e':
                print(f"Game over! ({start_row}, {start_col})")
                break
        else:
            start_row -= 1
else:
    print(f"{amount_coal} pieces of coal left. ({start_row}, {start_col})")
