nodes = int(input())
graph = {}
edges = []
for _ in range(nodes):
    node, children_str = input().split('->')
    children = children_str.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    print(source, destination)
    if destination not in graph[source] or source not in graph[destination]:
        continue

