def nested_loops(n, curr_iteration=[]):
    if len(curr_iteration) == n:
        print(*curr_iteration)
        return

    for i in range(1, n+1):
        nested_loops(n, curr_iteration + [i])

n = int(input())
nested_loops(n)
