# 크루스칼 알고리즘을 사용
# 전체 가로등을 켜는 비용 - 최소 신장 트리를 구성하는 비용

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0
total = 0

for i in range(n + 1):
    parent[i] = i
    
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    total += cost
    
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result += cost
        
print(total - result)