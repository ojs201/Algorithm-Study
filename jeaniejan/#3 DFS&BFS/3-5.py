from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
s,sx,sy = map(int,input().split())
q = []
move = [(0,1),(1,0),(0,-1),(-1,0)]

temp_q = [[] for _ in range(k+1)]
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            q.append((board[i][j],i,j))
# 번호가 작은 순서대로
q = deque(sorted(q))

while s:
    temp_q = deque()
    s-=1
    while q:
        num,x,y = q.popleft()
        for a,b in move:
            dx=x+a; dy=y+b
            if n>dx>=0 and n>dy>=0 and board[dx][dy] == 0:
                board[dx][dy] = num
                temp_q.append((num,dx,dy))
    if not temp_q:
        break
    q = temp_q
    
print(board[sx-1][sy-1])