# 최단거리 -> bfs 사용
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # n+1 개의 노르를 갖는 그래프 생성
distance = [0] * (n+1) # 출발 도시에서 각 도시까지의 최단 거리 저장을 위한 리스트 (1~n)
visited = [False] * (n+1) #방문 여부를 위한 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # print(graph)

def bfs(x, k):
    answer = [] # 최단거리 저장할 리스트 
    queue = deque()
    queue.append(x)
    distance[x] = 0
    visited[x] = True  # 시작 노드를 방문처리
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[now] + 1
                
                if distance[i] == k:
                    answer.append(i)
    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in range(len(answer)):
            print(answer[i])
        
bfs(x, k)