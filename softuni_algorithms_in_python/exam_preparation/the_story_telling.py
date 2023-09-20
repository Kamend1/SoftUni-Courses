from collections import defaultdict
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

graph = defaultdict(list)

while True:
    line = input()
    if line == "End":
        break

    line_path = line.split(' -> ')
    node = line_path[0]
    if len(line_path) > 1:  # Check if there are any postStories
        children = line_path[1].split(' ')
    else:
        children = []
    graph[node.rstrip(' ->')] = [child.rstrip(' ->') for child in children]

visited = set()
cycles = set()

sorted_nodes = deque()
for node in graph:
    dfs(node, graph, visited, cycles, sorted_nodes)

print(*sorted_nodes, sep=" ")

