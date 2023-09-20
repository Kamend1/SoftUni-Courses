def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_nodes_without_dependencies(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node
    return None

nodes = int(input())
graph = {}

for i in range(nodes):
    line_path = input().split(' ->')
    node = line_path[0].strip()
    if line_path[1]:
        children = line_path[1].strip().split(', ')
    else:
        children = []
    graph[node] = children

dependencies_by_node = find_dependencies(graph)

has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_nodes_without_dependencies(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

print(sorted_nodes)
