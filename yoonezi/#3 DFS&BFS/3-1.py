# 알고리즘:
#     모든 노드에 대하여 특정 지점에서 주변을 살피고 값이 0이며 방문하지 않은 노드를 방문
#     방문하지 않은 지점의 수 카운트


n ,m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]
result = 0


def dfs(x, y):
    # 탈출 할 경우
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if ice[x][y] == 0: # 뚫린 칸이라면
        ice[x][y] = 1 # 발문처리 해주고
        # 주변 노드들도 재귀적으로 호출    
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
            
            
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
