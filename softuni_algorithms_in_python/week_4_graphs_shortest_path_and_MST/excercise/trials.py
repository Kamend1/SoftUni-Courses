from collections import deque
from queue import PriorityQueue

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

nodes = int(input())
edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

source = int(input())
destination = int(input())

max_node = max(graph.keys())
weight = [0.0] * (max_node + 1)
parent = [None] * (max_node + 1)

weight[source] = 1.0
priority_queue = PriorityQueue()
priority_queue.put((-1.0, source))

while not priority_queue.empty():
    max_weight, node = priority_queue.get()
    if node == destination:
        break
    for edge in graph[node]:
        child = edge.destination if edge.source == node else edge.source
        new_weight = max_weight * (edge.weight / 100)
        if new_weight > weight[child]:
            weight[child] = new_weight
            parent[edge.destination] = node
            priority_queue.put((-new_weight, child))

if weight[destination] == 0.0:
    print('There is no such path.')
else:
    weight_to_print = weight[destination] * 100.0
    print(f'Most reliable path reliability: {weight_to_print:.2f}%')
    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=" -> ")
