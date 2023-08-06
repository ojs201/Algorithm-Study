from bisect import bisect_left, bisect_right
# 이진탐색
n, x =  map(int, input().split())
data = list(map(int, input().split()))


def bisect(array, left, right):
    right_index = bisect_right(array, right)
    left_index = bisect_left(array, left)
    return right_index - left_index

result = bisect(data, x, x)
if result == 0:
    print(-1)
else:
    print(result)