from collections import deque
from queue import PriorityQueue

class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest, forest_edges):
    forest.add(node)

    priority_queue = PriorityQueue()
    for edge in graph[node]:
        priority_queue.put(edge)

    while not priority_queue.empty():
        min_edge = priority_queue.get()
        non_tree_node = -1

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second
        elif min_edge.first not in forest and min_edge.second in forest:
            non_tree_node = min_edge.first

        if non_tree_node == -1:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)

        for edge in graph[non_tree_node]:
            priority_queue.put(edge)

nodes = int(input())
edges = int(input())
graph = {}

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

forest = set()
forest_edges = []
for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

distance = 0
for edge in forest_edges:
    distance += edge.weight

print(f'Total cost: {distance}')
