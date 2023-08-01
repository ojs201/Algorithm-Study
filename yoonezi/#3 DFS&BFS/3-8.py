# 참고하여 풀었음
# bsf > 재귀
# 상하좌우 dx, dy
# 백트래킹 ...
# 모든 빈 공간에 장애물 3개 설치하고 
# 쌤 위치에서 힉생이 탈출 가능한지 bfs탐색

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for teacher in t_loc:
        for i in range(4):
            nx, ny = teacher
            
            # if nx < 0 or nx >= n or ny < 0 or ny >= n:
            #     break
            # if graph[nx][ny] ==  "O":
            #     break
            # if graph[nx][ny] == "S":
            #     return False
            
            # ny += dy[i]
            # nx += dx[i]
            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == "O":
                    break

                if graph[nx][ny] == "S":
                    return False

                nx += dx[i]
                ny += dy[i]
    return True


def backTracking(cnt):
    global flag
    
    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        for x in range(n):
            for y in range(n):
                if graph[x][y] == "X":
                    graph[x][y] == "O"
                    backTracking(cnt + 1)
                    graph[x][y] == "X"
                
            
        



n = int(input())
graph =  []
t_loc = []
flag = False

for i in range(n):
    graph.append(list(map(str, input().split())))
    for j in range(n):
        if graph[i][j] == "T":
            t_loc.append([i,j])
            # print(t_loc)

backTracking(0)
if flag:
    print("YES")
else:            
    print("NO")
