from collections import deque
import math

class Edge:
    def __init__(self, from_currency, to_currency, price):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.price = price

def get_currency_index(currency_name):
    if currency_name not in currency_indices:
        currency_indices[currency_name] = len(currency_indices)
    return currency_indices[currency_name]

currencies = int(input())
graph = []

# Mapping to store integer indices for currency names
currency_indices = {}

for _ in range(currencies):
    from_currency, to_currency, price = input().split()
    price = -math.log(float(price))
    from_index = get_currency_index(from_currency)
    to_index = get_currency_index(to_currency)
    graph.append(Edge(from_index, to_index, price))

target_currency = input()
target_index = get_currency_index(target_currency)

distance = [float('inf')] * len(currency_indices)
parent = [None] * len(currency_indices)
distance[target_index] = 0

for i in range(len(currency_indices) - 1):
    updated = False
    for edge in graph:
        if distance[edge.from_currency] == float('inf'):
            continue
        new_distance = distance[edge.from_currency] + edge.price
        if new_distance < distance[edge.to_currency]:
            distance[edge.to_currency] = new_distance
            parent[edge.to_currency] = edge.from_currency
            updated = True
    if not updated:
        break

else:
    print('False')
    exit()

print('True')
path = deque()
node = target_index
while node is not None:
    currency_name = next((name for name, index in currency_indices.items() if index == node), None)
    if currency_name:
        path.appendleft(currency_name)
    node = parent[node]
print(*path, sep=" ")
print(math.exp(distance[target_index]))
