from collections import deque

#3-2.py
#BFS?

# N, M
n, m = map(int, input().split())

#보드 정의
board = []
for i in range(n):
    board.append(list(map(int, input())))

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(n):
            nx = x + dx[i]
            ny = y + dx[i]
            
            if nx == -1 or nx == n or ny == -1 or ny == m:
                continue
            if board[x][y] == 0:
                continue
            if board[nx][ny] == 1:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
    return board[n-1][m-1]
                    
print(bfs(0,0))
            
            