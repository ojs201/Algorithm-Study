# A번 학생의 성적이 B번 학생의 성적보다 낮다면, 
# 화살표가 A -> B 를 가르키도록 한다.
# 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램
# 모든 노드에 방문 가능한 노드를 찾기 ?

# 주어진 범위도 작고, 모든 노드 -> 다른 모든 노드까지의 경로를 구하는 문제 :: 플로이드 워셜 알고리즘

# 구현 순서:
#     1. 노드의 개수 및 간선의 개수 입력 받기
#     2. 2차원 리스트 만들고, 모든값을 무한으로 초기화
#     3. 자기 자신으로 가는 비용은 0으로 초기화
#     4. 각 간선에 대한 정보 입력 받고, 그 값으로 초기화
#     5. 거쳐갈 노드 x와 최종 목적지 노드 k 입력 받기
#     6. 플로이드 워셜 알골리즘 수행
#     7. 수행된 결과 출력

# 학생들의 수 = 노드의 개수 : n
# 두 학생의 성적을 비교한 횟수 = 간선의 개수 : m
# 성적이 낮은 학생 : a, 성적이 높은 학생 : b

# 노드의 개수 및 간선의 개수 입력 받기
n, m = map(int, input().split())

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
#2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 1로 초기화
    # : a 학생이 b 학생보다 낮은 순위에 있다는 의미
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
print(graph)       
         
#수행된 결과 출력 부분

result = 0
for a in range(1, n + 1):
    print("a: ", a)
    cnt = 0
    print("cnt :", cnt)
    for b in range(1, n + 1):
        print("b: ", b)   
        # a -> b || b -> a 경로가 있는지 확인
        if graph[a][b] != INF or graph[b][a] != INF:
            cnt += 1
            print(graph[a][b], graph[b][a])
            print("!= INF cnt :", cnt)
            
    if cnt == n:
        result += 1
        print("result: ",result)
        
print(result)