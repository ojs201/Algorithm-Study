# 병사 배치하기

import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

Lis = [arr[0]]

for i in range(1, n):
    num = arr[i]
    idx = bisect.bisect_left(Lis, num)

    if idx >= len(Lis):
        Lis.append(num)

    else:
        Lis[idx] = num

print(n - len(Lis))