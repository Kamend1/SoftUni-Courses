def find_minimum_sum_subsequence(sequence):
    n = len(sequence)
    if n <= 4:
        return sum(sequence)

    dp = [0] * n
    dp[0] = sequence[0]
    dp[1] = sequence[1]
    dp[2] = sequence[2]
    dp[3] = sequence[3]

    for i in range(4, n):
        dp[i] = min(dp[i-4], dp[i-3], dp[i-2], dp[i-1]) + sequence[i]

    return min(dp[-1], dp[-2], dp[-3], dp[-4])


sequence = list(map(int, input().split()))
result = find_minimum_sum_subsequence(sequence)
print(result)
