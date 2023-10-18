# n개의 집, m개의 간선, 유지비 > 크루스칼 알고리즘 - 최소 신장 트리 
# 2개의 분리된 마을로 분할
# 분리된 마을 안에 있는 집들은 모두 연결되어야 함
# 분리된 두 마을 사이에 있는 길들은 없앨 수 있음
# 나머지 길의 유지비의 합을 최소로 하고싶음

# 아이디어:
#     크루스칼 알고리즘으로 최소신장트리를 만든 후,
#     가장 비용이 큰 도로를 없애면 되는 문제
    
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
    return


n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i]= i
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
print(result - last)