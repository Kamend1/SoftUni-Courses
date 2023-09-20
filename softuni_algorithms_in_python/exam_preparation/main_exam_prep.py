from queue import PriorityQueue

class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

def prim(node, graph, forest, forest_edges, total_damage):
    forest.add(node)

    priority_queue = PriorityQueue()
    for edge in graph[node]:
        priority_queue.put(edge)

    while not priority_queue.empty():
        min_edge = priority_queue.get()
        non_tree_node = None

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second
        elif min_edge.first not in forest and min_edge.second in forest:
            non_tree_node = min_edge.first

        if non_tree_node is None:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)


        for edge in graph[non_tree_node]:
            priority_queue.put(edge)


nodes = int(input())
edges = int(input())
strikes = int(input())
graph = {}

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

total_damage = [0] * nodes
forest = set()
forest_edges = []
strikes_list = []

for _ in range(strikes):
    node, damage = [int(x) for x in input().split()]
    strikes_list[node].append(damage)
    print(strikes_list)

for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges, total_damage)

for edge in forest_edges:
    print(f'{edge.first} - {edge.second}')

highest_damage = max(total_damage)
print(highest_damage)
