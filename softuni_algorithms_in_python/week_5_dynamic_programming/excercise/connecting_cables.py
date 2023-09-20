from collections import deque

first = [int(x) for x in input().split()]
second = [pos for pos in range(1, len(first) + 1)]

rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row -1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(f"Maximum pairs connected: {dp[rows - 1][cols -1]}")
