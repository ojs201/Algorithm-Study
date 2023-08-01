# n-1개 연산자, + , - , x , % 
# 백트래킹문제 -> dfs
n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
# print(add, sub, mul, div);
answer = 0
maxValue = -int(1e9)
minValue = int(1e9)

def dfs(add, sub, mul, div, sum, index):
    global maxValue, minValue
    if index == n:
        maxValue = max(maxValue, sum)
        minValue = min(minValue, sum)
        return
    if add != 0:
        dfs(add-1, sub, mul, div, sum + num_list[index], index+1)
    if sub != 0:
        dfs(add, sub-1, mul, div, sum - num_list[index], index+1)
    if mul != 0:
        dfs(add, sub, mul-1, div, sum * num_list[index], index+1)
    if div != 0:
        dfs(add, sub, mul, div-1, int(sum / num_list[index]), index+1)

dfs(add, sub, mul, div, num_list[0], 1)
print(maxValue)
print(minValue)
        
        
        