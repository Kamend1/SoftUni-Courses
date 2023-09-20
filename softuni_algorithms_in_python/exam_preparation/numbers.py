def find_ways(N, current_way, current_sum, ways):
    if current_sum == N:
        ways.append(current_way)
        return

    for num in range(1, N - current_sum + 1, 1):
        if not current_way or num <= current_way[-1]:
            find_ways(N, current_way + [num], current_sum + num, ways)


N = int(input())
ways = []
find_ways(N, [], 0, ways)

for way in ways[::-1]:
    print(' + '.join(map(str, way)))
