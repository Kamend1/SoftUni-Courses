from collections import deque

def dfs(node, graph, visited, cycles, sorted_nodes):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


nodes = int(input())
graph = {}

for i in range(nodes):
    line_path = input().split(' ->')
    node = line_path[0].strip()
    if line_path[1]:
        children = line_path[1].strip().split(', ')
    else:
        children = []
    graph[node] = children

visited = set()
cycles = set()

sorted_nodes = deque()
for node in graph:
    dfs(node, graph, visited, cycles, sorted_nodes)

print(*sorted_nodes, sep=", ")
