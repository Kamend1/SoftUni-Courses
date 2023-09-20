from collections import deque

nodes = int(input())
edges = int(input())

graph = []

for _ in range(nodes + 1):
    graph.append([])

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
end_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == end_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()
node_travel = end_node
while node_travel is not None:
    path.appendleft(node_travel)
    node_travel = parent[node_travel]

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')
