import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수, 시작 노드
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보 담을 리스트
graph = [ [] for i in range(n+1) ]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split()) # x: 시작노드, y: 도착노드, z: 비용
    graph[x].append((y, z)) 

def dijkstra(start):
    q = []
    
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: 
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 방문했다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

#메세지수
count = 0
max_distance = 0 # 시간

for d in distance:
    if d != INF:
        count = count + 1
        max_distance = max(max_distance, d)
print(count - 1, max_distance)            