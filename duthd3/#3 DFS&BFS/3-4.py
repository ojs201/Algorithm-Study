#DFS?느낌
n, m = map(int, input().split())

###############보드판 만들기###############
board = []
for i in range(n):
    board.append(list(map(int, input())))
################보드판 만들기###############

# print(board)

dx = [-1, 1, 0, 1] # 상 하
dy = [0, 0, -1, 1] # 좌 우

# 바이러스 사방으로 퍼뜨리기
def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx>=0 and nx < n and ny >= 0 and ny < m):
            if board[nx][ny] == 0 : # 바이러스가 퍼질 수 있는 공간이면,
                board[nx][ny] = 2 # 바이러스를 퍼뜨린다.
                spread_virus(nx, ny)
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            board[i][j] = 2
            spread_virus(i, j)

print(board)