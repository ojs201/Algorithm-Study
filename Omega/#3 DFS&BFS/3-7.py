# 연산자 끼워넣기

def dfs(n, result, add, sub, mul, div):
    global mn, mx
    # 예외 처리
    if result < int(-1e9) or int(1e9) < result:
        return
    # 종료 조건
    if n == N:
        mn = min(mn, result)
        mx = max(mx, result)
        return
    if add > 0:
        dfs(n + 1, result + data[n], add - 1, sub, mul, div)
    if sub > 0:
        dfs(n + 1, result - data[n], add, sub - 1, mul, div)
    if mul > 0:
        dfs(n + 1, result * data[n], add, sub, mul - 1, div)
    if div > 0:
        dfs(n + 1, int(result / data[n]), add, sub, mul, div - 1)

N = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn = int(1e9)
mx = int(-1e9)

dfs(1, data[0], add, sub, mul, div)
print(mx, mn, sep = '\n')