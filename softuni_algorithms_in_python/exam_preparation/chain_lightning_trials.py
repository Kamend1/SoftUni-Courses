class Edge:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


def kruskal(graph, strikes):
    total_damage = [0] * (nodes + 1)
    isolated_damage = [0] * (nodes + 1)
    parent = [i for i in range(nodes + 1)]  # Initialize the parent array with each node as its own parent

    def apply_damage(node, damage, visited):
        visited.add(node)  # Mark the current node as visited
        root = find_root(parent, node)
        total_damage[root] += damage
        total_damage[node] = 0
        for edge in graph[node]:
            if edge.destination not in visited:
                apply_damage(edge.destination, damage // 2, visited)  # Assign half of the damage to the destination node

    forest = []
    for source, damage in strikes:
        if source in graph:
            for edge in sorted(graph[source], key=lambda e: e.distance):  # Sort the edges by distance for the current source node
                first_node_root = find_root(parent, edge.source)
                second_node_root = find_root(parent, edge.destination)

                if first_node_root != second_node_root:
                    parent[first_node_root] = second_node_root
                    forest.append(Edge(edge.source, edge.destination, edge.distance))
                    apply_damage(edge.destination, damage // 2, set())  # Assign half of the damage to the destination node
        else:
            isolated_damage[source] += damage  # Accumulate damage for isolated nodes

    # Process accumulated damage for isolated nodes
    for node, damage in enumerate(isolated_damage):
        if damage > 0:
            apply_damage(node, damage, set())

    return total_damage


nodes = int(input())
edges = int(input())
strikes_num = int(input())
strikes = []

graph = {}
for _ in range(edges):
    source, destination, distance = map(int, input().split())
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, distance))
    graph[destination].append(Edge(destination, source, distance))  # Undirected graph, add both directions

for _ in range(strikes_num):
    strike_node, damage = map(int, input().split())
    strikes.append((strike_node, damage))

total_damage = kruskal(graph, strikes)

highest_damage = max(total_damage)
print(highest_damage)
print(total_damage[0])  # Ignore the first element as it represents node 0, which is not used
