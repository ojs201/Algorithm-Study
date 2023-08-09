# 이중 포문 x
n = int(input())
arr = list(map(int ,input().split()))
arr.sort()
result = 0

for a in arr:
    if a == arr.index(a):
        result = a
        break
    else:
        result = -1
        
if result != 0:
    print(result)
else:
    print(-1)