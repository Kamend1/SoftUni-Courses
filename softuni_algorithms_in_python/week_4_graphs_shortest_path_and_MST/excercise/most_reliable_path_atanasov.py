from collections import deque
from queue import PriorityQueue

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    edge = Edge(source, destination, weight)
    graph[source].append(edge)
    graph[destination].append(edge)

start_node = int(input)
end_node = int(input)

pq = PriorityQueue()
pq.put((100, start_node))
