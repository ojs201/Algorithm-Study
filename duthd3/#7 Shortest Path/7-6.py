import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드를 입력
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [ [] for i in range(n+1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split()) 
    
    graph[a].append((b, 1)) # a에서 b로 가는 비용 1
    graph[b].append((a, 1)) # b에서 a로 가는 비용 1(양방향)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단거리가 짧은 노드 정보 꺼내온다.
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리가 되었다면
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)


max_node = 0 # 숨을 헛간 번호

max_distance = 0 # 최단 거리가 가장 먼 노드와의 최단거리

result = [] # 최단 거리가 가장 먼 헛간이 여러개일 때 저장

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
    
print(max_node, max_distance, len(result))
                            