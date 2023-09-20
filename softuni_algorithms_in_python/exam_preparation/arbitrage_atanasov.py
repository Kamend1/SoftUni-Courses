def extract_path(node, parent):
    first_node = node
    result = [node]
    while True:
        node = parent[node]
        result.append(node)
        if node == first_node:
            break
        result.append(node)

    return result



nodes = set()
edges = int(input())
graph = []

for _ in range(edges):
    source, destination, weight_as_string = input().split()
    weight = float(weight_as_string)
    graph.append((source, destination, weight))
    nodes.add(source)
    nodes.add(destination)
start_node = input()

distance = {node: float('-inf') for node in nodes}
distance[start_node] = 1

parent = {}

for _ in range(len(nodes) - 1):
    for (source, destination, weight) in graph:
        new_distance = distance[source] * weight
        if new_distance > distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source

for (source, destination, weight) in graph:
    new_distance = distance[source] * weight
    if new_distance > distance[destination]:
        print(True)
        path = extract_path(start_node, parent)
        print(*path, sep=" ")
        break
else:
    print(False)
    for node, best_price in distance.items():
        print(f'{node}: {best_price:.3f}')
