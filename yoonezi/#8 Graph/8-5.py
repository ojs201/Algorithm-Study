# 문제 자체가 이해가 안됐던 문제

# 문제 요약 :
#     비행기가 도킹할 수 있는 최대 탑승구에 도킹해감
#     도킹했으면, 최대 도킹 수를 줄임
    
# 아이디어 :
#     가능한 큰 번호의 탑승구로 도킹을 수행
#     > 탑승구 번호가 주어질 때,
#     최대한 큰 번호의 탑승구로 비행기를 보내는 것이 도킹할 수 있는 비행기 개수가 최대가 됨
#     도킹 = union
    
#     단, union 연산 시, 어떤 탑승구 번호로 연결해야 하는지는 풀이에서 임의대로 만들어 정보를 부여받은 탑승구 번호 기준으로 -1 만큼 작은 탑승구 
#     즉, 왼쪽에 있는 탑승구 번호로 연결해야 하도록 Union 연산을 하는 것으로 가정했다.(이걸 어떻게 시험장에서 떠올리지..? OMG다 증말..)
#     그리고 항상 부모 테이블을 만들 때, 0번 루트 노드가 자동으로 생기는데, 해
#     당 문제에서는 특정 탑승구 번호를 부여받았을 때, find 연산을 수행해서 0번 루트노드이면 더 이상 도킹할 수 없다는 것으로 룰을 만들었다..

g = int(input())
p = int(input())

# 탑승구를 하나의 집합으로 간주하고 서로소 집합 알고리즘 활용
parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i


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

count = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    # 만약 주어진 g_i값의 루트노드가 0이라면 더이상 탑승구에 들어갈 수 없고 운행 중지
    if data == 0:  # find_parent() 함수 넣으면 바로 첫번째 재귀함수 return이 반환되므로 재귀함수 == 0 조건은 안 됨!
        break
    # 루트노드가 0이 아니라면 주어진 주어진 탑승구 번호의 루트 노드와 루트 노드-1을 union연산
    union_parent(parent, data, data-1)
    count += 1

print(count)