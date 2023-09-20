from collections import deque

nodes = int(input())
pairs = int(input())

graph = []

[graph.append([]) for _ in range(nodes + 1)]

for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    queue = deque([source])
    visited = [False] * len(graph)
    visited[source] = True
    parent = [None] * len(graph)

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            queue.append(child)
            visited[child] = True
            parent[child] = node

    if parent[destination] is None:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    path = deque()
    node = destination
    size = 0
    while node is not None:
        path.appendleft(node)
        node = parent[node]
        size += 1

    print(f'{{{source}, {destination}}} -> {size - 1}')
