# 전체탐색 알고리즘(가능한 모든 경우를 고려하여 최적의 해를 찾는 방식)
# 모든 행을 순회하고 각 행의 최소값을 구하는 모든 경우를 확인하고 있음

n, m = map(int,input().split())
data = []

for i in range(n):
    row = list(map(int, input().split()))
    min_arr = min(row)
    data.append(min_arr)
     
print(max(data))