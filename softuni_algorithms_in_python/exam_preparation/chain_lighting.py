from collections import deque

class Edge:
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance

def prim(graph, start_node, damage, total_damage, visited):
    forest = set([start_node])
    queue = deque([(start_node, damage)])
    visited = set([start_node])

    while queue:
        current_node, current_damage = queue.popleft()

        total_damage[current_node] += current_damage

        if current_node in graph:
            for edge in graph[current_node]:
                neighbor = edge.destination
                if neighbor not in forest:
                    new_damage = current_damage // 2
                    queue.append((neighbor, new_damage))
                    forest.add(neighbor)
                    visited.add(neighbor)

nodes = int(input())
edges = int(input())
strikes = int(input())
graph = {}

for _ in range(edges):
    source, destination, distance = map(int, input().split())
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(destination, distance))
    graph[destination].append(Edge(source, distance))

total_damage = [0] * nodes

for _ in range(strikes):
    start_node, damage = [int(x) for x in input().split()]
    prim(graph, start_node, damage, total_damage, set())

highest_damage = max(total_damage)
print(highest_damage)
print(total_damage)
