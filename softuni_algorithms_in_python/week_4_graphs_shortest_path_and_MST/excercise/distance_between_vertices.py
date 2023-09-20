from collections import deque


def map_node(node):
    if node not in node_map:
        node_map[node] = consecutive_node_num[0]
        consecutive_node_num[0] += 1
    return node_map[node]


nodes = int(input())
number_pairs = int(input())

# Create a dictionary to map input node numbers to consecutive numbers
node_map = {}
consecutive_node_num = [1]

graph = {}
pairs_to_analyze = []

for _ in range(nodes):
    line = input().split(':')
    node = int(line[0])
    children = [int(child) for child in line[1].split()] if len(line) > 1 else []
    graph[map_node(node)] = [map_node(child) for child in children]

for _ in range(number_pairs):
    source, destination = [int(x) for x in input().split('-')]
    pairs_to_analyze.append((map_node(source), map_node(destination)))

for pair in pairs_to_analyze:
    start_node = pair[0]
    end_node = pair[1]

    visited = [False] * (consecutive_node_num[0])
    parent = [None] * (consecutive_node_num[0])

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

    if len(path) == 1:
        print(
            f'{{{list(node_map.keys())[list(node_map.values()).index(start_node)]}, {list(node_map.keys())[list(node_map.values()).index(end_node)]}}} -> -1')
    else:
        print(
            f'{{{list(node_map.keys())[list(node_map.values()).index(start_node)]}, {list(node_map.keys())[list(node_map.values()).index(end_node)]}}} -> {len(path) - 1}')
