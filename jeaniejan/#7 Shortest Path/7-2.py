#전보
import heapq

# 도시 개수 n, 경로 개수 m, 메시지를 보낸 도시 c
n, m, c = map(int, input().split())
# 한 도시에서 다른 도시로 가는 시간 list
city = [list(map(int, input().split())) for _ in range(m)]

INF = int(1e9) # 무한을 의미하는 값 10억 설정

# 각 도시에 연결되어 있는 도시에 대한 정보를 담을 list 설정
graph = [[] for _ in range(n + 1)]
# 최단 시간 테이블을 모두 무한으로 초기화
time = [INF] * (n + 1)

# 모든 연결 정보를 저장
# i[0]: 출발 도시, i[1]: 도착 도시, i[2]: 소요 시간
# 꼭 append 함수를 쓸 것!
for i in city:
	graph[i[0]].append((i[1], i[2]))
    
def dijkstra(start):
	q = []
	# 시작 도시로 가기 위한 최단 시간은 0으로 설정하여 큐에 삽입
	heapq.heappush(q, (0, start))
	time[start] = 0
	
	while q: # 큐가 비어있지 않다면
		# 가장 최단 시간이 짧은 도시에 대한 정보 꺼내기
		t, now = heapq.heappop(q)
		# 현재 도시가 이미 처리된 적 있다면(즉, 이미 최단 시간이라면), 무시
		if time[now] < t:
			continue
            
		# 현재 도시와 연결된 다른 인접 도시들을 확인
		for j in graph[now]:
			# 현재 도시까지의 최단 시간(t) 
            # + 현재 도시에서 다른 도시(j[0])까지 걸리는 시간(j[1])
			cost = t + j[1]
			# 현재 도시를 거쳐서 다른 도시로 가는 시간이 더 짧은 경우
			if cost < time[j[0]]:
				time[j[0]] = cost # 더 짧은 시간으로 갱신
				# j[0]으로 가기 위한 최단 시간은 cost로 설정하여 큐에 삽입
				heapq.heappush(q, (cost, j[0]))
	
	time_no_INF = [i for i in time if i != INF] # time list에서 무한을 삭제한 list 생성
    # 출발 도시가 보낸 메시지를 받는 도시의 총 개수(출발 도시는 제외하기 위해 -1을 함)
	city_n = len(time_no_INF) - 1
    # 메시지를 받는데 총 걸리는 시간(즉, 출발 도시에서 가장 오랜 시간이 걸리는 경우)
	time_sum = max(time_no_INF)
    
	return print(city_n, time_sum, sep = ' ')
    
dijkstra(c)