# bfs ...?
# 상하좌우 비교하기 

from collections import deque


n, l, r = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]    
dy = [0, 0, -1, 1]
    
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    sum_country =  [(x, y)]
    count = country[x][y]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visit[nx][ny]:
                continue
            # if l <= country[x][y] - country[nx][ny] <= r or l <= country[nx][ny] - country[x][y] <= r:
            if l <= abs(country[x][y] - country[nx][ny]) <= r:
                sum_country.append((nx, ny))
                visit[nx][ny] = True
                queue.append((nx, ny))
                count += country[nx][ny]
    for a, b in sum_country:
        country[a][b] = count // len(sum_country)
            
            
    return len(sum_country)

result = 0
while True:
    visit = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    result += 1

print(result)

