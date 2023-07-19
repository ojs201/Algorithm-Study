n, m = map(int, input().split())
x, y, d = map(int, input().split())

dir = [0, 3, 2, 1]  # 시계 반대 방향 (북서남동)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

arr = []
cnt = 1
for i in range(n):
    arr.append(list(map(int, input().split())))

idx = dir.index(d)+1
while(1):
    arr[y][x] = 1
    nx = x + dx[idx]
    ny = y + dy[idx]

    if arr[ny][nx] == 0:
        x = nx
        y = ny
        arr[ny][nx] = 1
        cnt += 1

    if idx < 3:
        idx += 1
    else:
        idx = 0
    
    count_n = 0
    for i in arr:
        if 0 not in i:
            count_n += 1
    if count_n == n:
        break

print(cnt)