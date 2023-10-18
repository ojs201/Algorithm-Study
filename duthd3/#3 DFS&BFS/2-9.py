n = int(input())
k = int(input())
direction_info = [] # 방향 회전 정보
# 보드 판
board = [[0] * (n+1) for _ in range(n+1)]

# 사과의 위치를 입력
for i in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1 #사과가 있으면 1

l = int(input()) # 방향 변환 횟수
for _ in range(l):
    x, c = input().split()
    direction_info.append((int(x), c))

# 동, 서, 남, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c): #현재 어디를 보고있고, 어디로(왼쪽, 오른쪽) turn 할지
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 위치는 2
    direction = 0 # 처음엔 동쪽
    time = 0 # 시작한 뒤에 지난 초
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx<= n and 1 <= ny and ny <= n and board[nx][ny] != 2:# 맵 범위 안에 있고, 뱀의 몸통이 없는 위치
            if board[nx][ny] == 0: #사과가 없다
                board[nx][ny] = 2
                q.append((nx, ny)) 
                px, py = q.pop(0) #꼬리를 큐에서 제거
                board[px][py] = 0 #꼬리를 보드에서 제거
            if board[nx][ny] == 1: #사과가 있다
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < 1 and time == direction_info[index][0]: #회전할 시간이라면
            direction = turn(direction, direction_info[index][1])
            index += 1
    return time

print(simulate())