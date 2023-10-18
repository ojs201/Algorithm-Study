# 다익스트라 알고리즘:
#     1. 출발 노드를 설정
#     2. 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
#     3. 최단 거리 테이블을 초기화
#     4. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
#     5. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
#     6. 4, 5번 반복

# 시작노드 : [0][0], 도착노드 : [n-1][n-1]

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 테스트 케이스 개수 t 입력 받기
t = int(input())

for _ in range(t):

    # 공간 n 입력 받기
    n = int(input())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
    # graph = [[] for i in range(n)]
    graph = []
    # 최단 거리 테이블은 모두 무한으로 초기화
    # distance = [INF] * (n + 1)

    # 모든 간선 정보 입력 받기
    for i in range(n):
        # a, b, c = map(int, input().split())
        graph.append(list(map(int, input().split())))
    # print(graph)
        
    distance = [[INF] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # 시작 위치
    x, y = 0, 0

    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 반복문으로 다익스트라 알고리즘 수행
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
                
    print(distance[n-1][n-1])