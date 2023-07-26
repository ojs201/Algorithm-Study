# 뱀

size = int(input())
apple_num = int(input())
apple_locate = [[0] * (size + 1) for _ in range(size + 1)] # 맵 정보
direction_info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(apple_num):
    a, b = map(int, input().split())
    apple_locate[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    direction_info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    apple_locate[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= size and 1 <= ny and ny <= size and apple_locate[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if apple_locate[nx][ny] == 0:
                apple_locate[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                apple_locate[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if apple_locate[nx][ny] == 1:
                apple_locate[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == direction_info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, direction_info[index][1])
            index += 1
    return time

print(simulate())
