def find_parent(graph, a):
    if graph[a] != a:
        graph[a] = find_parent(graph, graph[a])
    return graph[a]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []
result = []

for i in range(1, n+1):
    parent[i] = i

    
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result.append(cost)
        
result.sort()
print(sum([i for i in result[:-1]]))