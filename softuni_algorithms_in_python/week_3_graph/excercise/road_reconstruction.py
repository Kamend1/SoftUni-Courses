def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


buildings_nodes = int(input())
streets_edges = int(input())

graph = []
edges = set()
for _ in range(buildings_nodes):
    graph.append([])

for _ in range(streets_edges):
    source, destination = input().split(' - ')
    source = int(source)
    destination = int(destination)
    graph[source].append(destination)
    graph[destination].append(source)
    edges.add((min(source, destination), max(source, destination)))

important_streets = []
for source, destination in edges:
    graph[source].remove(destination)
    graph[destination].remove(source)

    visited = [False] * buildings_nodes
    dfs(0, graph, visited)

    if not all(visited):
        important_streets.append((source, destination))

    graph[source].append(destination)
    graph[destination].append(source)

print('Important streets:')
for first, second in important_streets:
    print(f'{first} {second}')
