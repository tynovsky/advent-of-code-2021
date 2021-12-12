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
    if node.lower() == node:
        for v in visited.values():
            if node in visited and v > 1:
                return []
        if node not in visited:
            visited[node] = 0
        if visited[node] > 0 and node == 'start':
            return []
        visited[node] += 1
    routes = []
    for next in nodes[node]:
        for route in find_routes(nodes, next, visited.copy()):
            routes.append([node] + route)
    return routes

routes = find_routes(nodes, 'start', {})
for r in routes:
    print(','.join(r))
print(len(routes))
