# 1. 뱀의 이동 : 2차원 배열상의 특정 위치에서 동서남북 위치 이동 기능 구현
# 2. 뱀의 처음 방향 : 동쪽
# 3. 뱀의 머리가 몸에 닿는 경우도 종료 고려 -> 매 시점마다 뱀의 위치 기록

from collections import deque
# 보드의 크기
n = int(input())
# 사과의 개수
k = int(input())
# 0으로 초기화딘 2차원 리스트 (n*n) 생성
board = [[0]*n for _ in range(n)]
# k개의 사과가 있는 곳
for _ in range(k):
    a, b = map(int, input().split())
    # 사과가 있는 좌표에 1 포시
    board[a-1][b-1] = 1
    
# 뱀의 방향 변환 횟수
l = int(input())
# 변환하는 방향 저장할 배열
turn = []
# t: t초 후 , d: 방향 회전
for _ in range(l):
    t, d = map(str, input().split())
    turn.append((int(t), d))
    
# 방향 설정 // 동,남,서,북 (뱀읨 머리가 동쪽부터임을 고려)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 현재 방향 : 오른쪽
nd = 0
# 뱀의 머리 위치(행: x,열 :y)
nx, ny = 0, 0
# 시간
time = 0 
# 뱀의 방향 전환 정보 인덱스
i = 0

# 뱀의 위치를 queue 자료구조로 표현
# 뱀의 현재 방향으로 전진하면 해당 좌표를 queue에 push
# 사과가 없어 꼬리를 옮겨야할 때는 queue의 첫번째 원소를 pop

queue = deque()
# 처음위치 넣어주기
queue.append((nx, ny))

while 1:
    # 현재 위치(x,y)에 입렵된 방향 더하기
    nx += dx[nd]
    ny += dy[nd]
    # 움직일때 1초씩 시간 증가
    time += 1
    # 보드위에서 벗어날때, 머리가 몸에 닿았을 때 멈춤
    if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) in queue:
        break
    queue.append((nx, ny))
     # 사과가 없을 경우 처리
    if board[nx][ny] == 0: 
        queue.popleft()
    else:
        # 사과 먹고 해당 자리 0으로 반환
        board[nx][ny] = 0
    #반황전환
    # 동 : 0, 남 : 1 ,서 : 2, 북 : 3
    if time == turn[i][0]:
        if turn[i][1] == "L":
            nd = (nd - 1) % 4
        else:
            nd = (nd + 1) % 4
        if i + 1 < len(turn):
            i += 1
            
print(time)