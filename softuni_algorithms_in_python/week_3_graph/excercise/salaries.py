def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1
    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    salaries[node] = salary
    return salary

nodes = int(input())
graph = []

for i in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)
    graph.append(children)

salaries = [None] * nodes

total_salary = 0
for node in range(nodes):
    salary = dfs(node, graph, salaries)
    total_salary += salary

print(total_salary)
