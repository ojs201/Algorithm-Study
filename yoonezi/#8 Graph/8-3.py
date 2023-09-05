# 문제요약 :
#     선수강의를 들어야 해당 강의를 들을 수 있음 -> "위상정렬 알고리즘"
#     강의는 1 ~ N번의 번호를 가짐
#     N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 출력
    
# "위상정렬 알고리즘 ?"
#     - 정렬 알고리즘의 일종
#     - 순서가 정해져있는 일련의 작업을 차례대로 수행해야 할 때 사용
#     - 대표적인 예시로, 선수과목을 고려한 학습순서 설정
#     - ✨ 진입차수 ✨ : 특정한 노드로 들어오는 간선의 개수를 의미
#     - 큐를 이용함
    
#     1. 진입차수가 0인 모든 노드를 큐에 넣는다.
#     2, 큐가 빌 때까지 다음의 과정을 반복한다.
#         1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
#         2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
#         > 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.

# 핵심 아이디어 :
#     각 강의에 대하여 인접한 노드를 확인하면서 인접한 노드에 대해
#     현재보다 강의 시간이 더 걸린 경우를 찾는다면, 해당 시간으로 결과 테이블 갱신 
    
# deepcopy ?
#  deepcopy는 객체를 복사할 때 해당 객체의 모든 요소와 중첩된 객체까지 모두 새로운 복사본을 생성하여 복사합니다. 
#  따라서 원본과 복사본은 완전히 독립적인 데이터를 가지게 됩니다.

#  result 리스트는 각 강의를 듣는 데 걸리는 최대 시간을 저장하는데,
#  이 정보는 time 리스트와 공유하지 않고 독립적으로 관리해야 합니다. 
#  그래서 copy.deepcopy() 함수를 사용하여 time 리스트를 복사하고, 
#  이 복사본을 result 리스트에 할당함으로써 두 리스트가 서로 영향을 미치지 않도록 보장합니다.

from collections import deque
import copy

n = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(n + 1)]
# 각 강의 시간 정보를 담기 위한 리스트 0으로 초기화
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 해당 노드에 시간 저장
    for x in data[1: -1]: # 해당 강의의 선행 강의 목록이 저장
        graph[x].append(i) # 선수과목이 x 이니, x -> i
        # print(" graph[x]",  x, graph[x])
        indegree[i] += 1 # 진입 차수는 들어오는 노드 입장이므로, i
        # print(" indegree[i] ",  i, indegree[i] )
        
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            # print("result[i]", result[i])
            
            # max(result에 업데이트된 인접 노드 시간, result에 업데이트된 현재 노드 시간 + 인접노드의 시간)
            result[i] = max(result[i], result[now] + time[i])
            # print(" result[now] + time[i]",  result[now] + time[i])
            # 해당 원소와 연결된 노드들의 진입차수에서 1뺴기
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    for r in result[1:]:
        print(r)

topology_sort()