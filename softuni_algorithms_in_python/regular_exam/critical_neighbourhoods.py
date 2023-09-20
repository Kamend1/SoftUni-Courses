from collections import deque
from queue import PriorityQueue

roads = int(input())
graph = {}

for i in range(roads):
    source, destination, distance_str = input().split(' - ')
    distance = int(distance_str)
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append((destination, distance))
    graph[destination].append((source, distance))

closed_roads = input().split(',')
for j in closed_roads:
    closed_source, closed_destination = j.split('-')
    closed_source = closed_source.strip()
    closed_destination = closed_destination.strip()

    if closed_source in graph:
        graph[closed_source] = [road for road in graph[closed_source] if road[0] != closed_destination]

    if closed_destination in graph:
        graph[closed_destination] = [road for road in graph[closed_destination] if road[0] != closed_source]

start_city = input()
end_city = input()

distance = {node: float('inf') for node in graph}
parent = {node: None for node in graph}

distance[start_city] = 0
priority_queue = PriorityQueue()
priority_queue.put((0, start_city))

while not priority_queue.empty():
    min_distance, node = priority_queue.get()
    if node == end_city:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge[1]
        if new_distance < distance[edge[0]]:
            distance[edge[0]] = new_distance
            parent[edge[0]] = node
            priority_queue.put((new_distance, edge[0]))

if distance[end_city] == float('inf'):
    print('There is no such path.')
else:

    path = deque()
    node = end_city
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=" - ")
    print(distance[end_city])
