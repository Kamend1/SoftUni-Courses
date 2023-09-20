def dfs(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


N = int(input())
M = int(input())

graph = {i: [] for i in range(N + 1)}

for _ in range(M):
    from_node, to_node = map(int, input().split())
    graph[from_node].append(to_node)

start_node = int(input())

visited = [False] * (N + 1)
visited[0] = True
dfs(start_node, graph, visited)

unreachable_outposts = [node for node in range(N + 1) if not visited[node]]

for node in unreachable_outposts:
    print(node, end=" ")
