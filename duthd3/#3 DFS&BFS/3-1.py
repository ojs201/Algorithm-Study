# 음료수 얼려 먹기

# 얼음 틀의 세로 길이 N, 가로길이 M

n, m = map(int, input().split())

# 얼음 틀의 형태 입력 받기
board = []
for i in range(n):
    board.append(list(map(int, input())))

# print(board)

dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

# 아이스크림 갯수
count = 0

#dfs
def dfs(x, y):
    board[x][y] = 1 #현재 노드 방문 처리
    # 현재 노드와 인접한 모든 노드 탐색, 방문
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx>= 0 and nx < n and  ny >= 0 and ny < m): # 인접 노드가 보드 안에 있고,
            if (board[nx][ny] == 0): # 방문 가능하면
                dfs(nx, ny) # 방문처리

for i in range(n):
    for j in range(m):
        if (board[i][j] == 0) : # 방문이 안 되었으면?
            dfs(i, j) # 인접노드 싹 다 돈 후에,
            count += 1 # 카운트 증가 시킴 그리고 이후에 방문 된 노드는 1로 바뀌니깐 0만 알아서 잘 찾아다닌다.

print(count)