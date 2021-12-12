import sys

nodes = {}

for line in sys.stdin:
    (node1, node2) = line.strip().split('-')
    if node1 not in nodes:
        nodes[node1] = []
    if node2 not in nodes:
        nodes[node2] = []

    nodes[node1].append(node2)
    nodes[node2].append(node1)

print(nodes)

def find_routes(nodes, node, visited):
    if node == 'end':
        return [['end']]
    visited.add(node)
    routes = []
    for next in nodes[node]:
        if next.lower() == next and next in visited:
            continue
        for route in find_routes(nodes, next, visited.copy()):
            routes.append([node] + route)
    return routes

routes = find_routes(nodes, 'start', set())
print(routes)
print(len(routes))
