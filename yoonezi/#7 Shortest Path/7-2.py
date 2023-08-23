# 아이디어 :
#     1. 한 도시에서 다른 도시까지의 최단 거리 문제로 치환 가능
#     2. n과 m 범위가 충분히 크기 때문에 우선순위 큐를 활용한 다익스트라 알고리즘 구현
    
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한(10억)으로 설정

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        print(" heapq.heappop(q) - dist: ", dist, "now : ", now)
        # 최단 거리 테이블(distance)에 담긴 now 노드의 값이 heapq에 들어있는 dist 거리보다 작다면 패스!
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            print("graph[now]: ", graph[now], "i: ", i)
            cost = dist + i[1]
            print("dist: ", dist, "i[1]", i[1])
            # 현재 노드들을 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                print("if cost < distance[i[0]]: >> 실행")
                print("distance[i[0] : ", distance[i[0]])
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# =========== 입력부분 ============

# 노드의 개수, 간선의 개수, 시작 노드 입력 받기
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
print("graph:", graph)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)
print("distance:", distance)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))
    print(graph)

# ===============================

# 다익스트라 알고리즘 수행 - 시작노드 : start
dijkstra(start)

# 도달할 수 있는 노드의 개수
cnt = 0

# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_dist = 0

for d in distance:
    if d != 1e9:
        cnt += 1
        max_dist = max(max_dist, d)
        
print( cnt - 1, max_dist)