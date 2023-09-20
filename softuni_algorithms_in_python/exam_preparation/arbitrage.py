from collections import defaultdict
import math

def find_arbitrage_trading_pairs(graph, target_currency):

    for from_currency in graph:
        for to_currency in graph[from_currency]:
            graph[from_currency][to_currency] = -math.log(graph[from_currency][to_currency])


    distance = {currency: float('inf') for currency in graph}
    distance[target_currency] = 0

    parent = {currency: None for currency in graph}

    for _ in range(len(graph) - 1):
        for source, destinations in graph.items():
            for destination, weight in destinations.items():
                if distance[source] + weight < distance[destination]:
                    distance[destination] = distance[source] + weight
                    parent[destination] = source

    # Check for negative-weight cycle
    arbitrage_currency = None
    for source, destinations in graph.items():
        for destination, weight in destinations.items():
            if distance[source] + weight < distance[destination]:
                arbitrage_currency = destination
                break

    if arbitrage_currency is not None:
        cycle = [arbitrage_currency]
        node = parent[arbitrage_currency]
        while node != arbitrage_currency:
            cycle.append(node)
            node = parent[node]
        cycle.append(arbitrage_currency)
        return True, cycle

    return False, None

currencies = int(input())
graph = {}

for _ in range(currencies):
    from_currency, to_currency, price = input().split()
    price = float(price)
    if from_currency not in graph:
        graph[from_currency] = {}

    graph[from_currency][to_currency] = price

target_currency = input()

arbitrage_possible, best_path = find_arbitrage_trading_pairs(graph, target_currency)

if arbitrage_possible:
    print("True")
    print(*best_path)
else:
    print("False")
    print("\n".join(f"{currency}: {rate:.3f}" for currency, rate in graph[target_currency].items()))
