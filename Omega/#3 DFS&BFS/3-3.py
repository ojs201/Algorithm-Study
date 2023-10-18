# 특정 거리의 도시 찾기

import sys
from collections import deque

input = sys.stdin.readline

# n 도시 수, m 도로 수, k 거리 정보 x 출발 도시
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 도로 정보 입력받기
for _ in range(m):
  a, b =  map(int, input().split()) # a와 b는 두 도시를 의미
  graph[a].append(b) # a에서 b로 가는 도로가 존재한다는 의미

# 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# BFS 구현
q = deque([x])
while q:
    now = q.popleft() # 현재 도시
    # 현재 도시에서 이동 가능한 도시 확인
    for next in graph[now]:
        # 아직 방문하지 않은 도시라면 최단거리 갱신
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

# 최단거리가 k인 도시번호 출력, 없다면 -1 출력
if k in distance:
  for i in range(1, n + 1):
    if distance[i] == k:
      print(i)
else:
  print(-1)

print(distance)
