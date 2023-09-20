from math import ceil, floor
n = int(input())

# roof
for row in range(1, ((n + 1) // 2) + 1):
    if n % 2 == 0:
        print("-" * ((n - 2 * row) // 2) + "*" * 2 * row + "-" * ((n - 2 * row) // 2))
    elif n % 2 != 0:
        print("-" * int((n - ((2 * row) - 1)) / 2) + "*" * row + "*" * (row - 1) + "-" * int((n - ((2 * row) - 1)) / 2))

# body of the house
if n == 2:
    print(chr(124) + chr(124))
elif n % 2 == 0:
    for row_house in range(ceil(n / 2 -1) + 1):
        print(chr(124) + "*" * (n - 2) + chr(124))
elif n % 2 != 0:
    for row_house in range(ceil(n / 2 -1)):
        print(chr(124) + "*" * (n - 2) + chr(124))
