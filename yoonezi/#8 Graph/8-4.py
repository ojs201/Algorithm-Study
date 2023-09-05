# 문제 요약 :
#     1 ~ n개의 여행지
#     하나의 여행 계획을 세운 뒤, 이 여행 계획이 가능한지 여부를 판단
    
# 아이디어 :
#     양방향 ..? 
#     입력 받으면서, 0 ~ n-1 노드에 1이면 index 값을 저장하고 ..
#     부모 찾아가기 ?
#     > 서로소 집합 자료구조 사용해보자

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
for i in range(n + 1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)
            
plan =  list(map(int, input().split()))

def possible(center):
    for p in plan:
        if center != find_parent(parent, p):
            return "NO"
        return "YES"
print(possible(find_parent(parent, plan[0])))