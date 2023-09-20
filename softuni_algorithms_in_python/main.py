from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight, connected):
        self.first = first
        self.second = second
        self.weight = weight
        self.connected = connected

    def __gt__(self, other):
        return self.weight > other.weight


def prim(graph, start, budget, used_budget):
    visited = set()
    current_node = start
    visited.add(current_node)

    priority_queue = PriorityQueue()
    for neighbor in graph[current_node]:
        if not neighbor.connected and neighbor.weight <= budget - used_budget:
            priority_queue.put(neighbor)

    while not priority_queue.empty():
        min_edge = priority_queue.get()
        non_tree_node = -1

        if min_edge.first in visited and min_edge.second not in visited:
            non_tree_node = min_edge.second
        elif min_edge.first not in visited and min_edge.second in visited:
            non_tree_node = min_edge.first

        if non_tree_node == -1:
            continue

        used_budget += min_edge.weight
        visited.add(non_tree_node)
        forest_edges.append(min_edge)

        for neighbor in graph[non_tree_node]:
            if neighbor.connected and neighbor.weight <= budget - used_budget:
                priority_queue.put(neighbor)

    return used_budget

budget = int(input())
nodes = int(input())
edges = int(input())
graph = {}
visited = set()
forest_edges = []

for _ in range(edges):
        line = input().split()
        if len(line) == 4:
            first = int(line[0])
            second = int(line[1])
            weight = int(line[2])
            connected = True
        else:
            first = int(line[0])
            second = int(line[1])
            weight = int(line[2])
            connected = False

        if first not in graph:
            graph[first] = []
        if second not in graph:
            graph[second] = []

        edge = Edge(first, second, weight, connected)
        graph[first].append(edge)
        graph[second].append(edge)


used_budget = 0
for node in graph:
    if node in visited:
        continue
    used_budget = prim(graph, node, budget, used_budget)

print(f'Budget used: {used_budget}')
