# 상하좌우 모든 방향으로 한번에 증식 -> dx, dy
# 순서가 낮은 바이러스가 더 먼저 증식
# > ex) 1과 2가 같은 곳에 증식 한다면 숫자를 비교하여 더 낮은 숫자를 배정
# BFS알고리즘 사용

from collections import deque

# 입력
n, k = map(int, input().split())

graph = [] # 시험관 정보 저장 리스트
virus = [] # 바이러스 정보 저장 리스트 

for i in range(n):
    #  raw = [list(map(int, input().split()))]
     graph.append(list(map(int, input().split())))     
     for j in range(n):
        #  바이러스 라면 해당 바이러스에 대한 정보 저장
        if graph[i][j] != 0:
            # 바이러스 숫자, 확산 시간, x 좌표, y 좌표
            virus.append((graph[i][j], 0, i, j))
            # print(virus)

# 바이러스 숫자 오름차순 정렬
virus.sort()
# 바이러스 정보를 큐로 변환
queue = deque(virus)

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# queue가 빌 때까지
while queue:
    # 바이러스 숫자, 확산 시간, 현재 좌표
    num, time, i, j = queue.popleft()

    # s초까지 확산 됐을 경우 
    if (time == s):
        break
    
    # 확산
    for l in range(4):
        nx = i + dx[l]
        ny = i + dy[l]
        # 범위가 아닌 경우 처리
        if ( nx < 0 or nx >= n or ny < 0  or ny >= n):
            break
        else:
            graph[nx][ny] = num
            queue.append((num, time+1, nx, ny))
            

print(graph[x-1][y-1])