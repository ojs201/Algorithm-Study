# 이중 for문 x
# 선형탐색x, 이진탐색으로

from bisect import bisect_left, bisect_right

def countNum(arr, left, right):
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(countNum(arr, m, m))


