import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]    
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

dijkstra(start)

max_node = 0
max_dist = 0
max_node_list = []
for i in range(1, n+1):
    if max_dist < distance[i]:
        max_node = i
        max_dist = distance[i]
        max_node_list = [max_node]
    elif max_dist == distance[i]:
        max_node_list.append(i)

print(max_node, max_dist, len(max_node_list))
