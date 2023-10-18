# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산
# 2차원 테이블에 최단 거리 정보를 저장
# 각 단계마다 특정한 노드 k를 거쳐가는 경우를 확인

# 구현 순서:
#     1. 노드의 개수 및 간선의 개수 입력 받기
#     2. 2차원 리스트 만들고, 모든값을 무한으로 초기화
#     3. 자기 자신으로 가는 비용은 0으로 초기화
#     4. 각 간선에 대한 정보 입력 받고, 그 값으로 초기화
#     5. 거쳐갈 노드 x와 최종 목적지 노드 k 입력 받기
#     6. 플로이드 워셜 알골리즘 수행
#     7. 수행된 결과 출력
    
# 도시의 수 = 노드의 개수 : n
# 버스의 개수 = 간선의 개수 : m
# 시작도시 : a, 도착 도시 : b, 한번 타는데 필요한 비용 : c

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b, c = map(int, input().split())
    # graph[a][b] = c
    graph[a][b] = min(c, graph[a][b]) # 시작도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다. > 최소값으로 넣기

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")
    print()