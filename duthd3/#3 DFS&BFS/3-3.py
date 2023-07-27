from collections import deque
#도시의 개수, 도로의 개수, 거리정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # 도시들 그래프
result = []
for i in range(m):
    a , b = map(int,input().split())
    graph[a].append(b)
    

# k가 최단거리인데, 최단거리가 중요
# x로부터 출발하여 도달할 수 있는 도시중에서, 최단거리가 k인 
# bfs 느낌.(모든 간선의 비용이 같기 때문에)

short_path = [-1]*(n+1) # 출발도시에서 각 도시로 갈때의 비용을 저장
short_path[x] = 0 #출발 도시 까지는 0

queue = deque([x])


    
while queue:
    now_city = queue.popleft() #현재도시
        
    for neighbor in graph[now_city]: # 현재 도시에서 이동 가능한 도시들 중에서
        if short_path[neighbor] == -1: # 방문하지 않았다면
            short_path[neighbor] = short_path[now_city] + 1 #현재 도시까지의 비용에서 비용 한 개 추가
            queue.append(neighbor)
            


##########################                  
for i in range(n+1):
    if short_path[i] == k:
        result.append(i)
        
result.sort()

if len(result) == 0:
    print(-1)
else:
    for i in range(len(result)):
        print(result[i])


