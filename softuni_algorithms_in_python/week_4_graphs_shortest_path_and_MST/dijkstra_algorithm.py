from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance

edges = int(input())
graph = {}

for i in range(edges):
    source, destination, distance = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, distance))

start_node = int(input())
end_node = int(input())

max_node = max(graph.keys())
distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start_node] = 0
priority_queue = PriorityQueue()
priority_queue.put((0, start_node))

while not priority_queue.empty():
    min_distance, node = priority_queue.get()
    if node == end_node:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.distance
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            priority_queue.put((new_distance, edge.destination))

if distance[end_node] == float('inf'):
    print('There is no such path.')
else:
    print(distance[end_node])
    path = deque()
    node = end_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=" ")
