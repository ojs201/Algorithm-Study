"""
4-7. 카드 정렬하기
https://www.acmicpc.net/problem/1715

1.
"""
from sys import stdin
from heapq import heapify, heappush, heappop

# E.G. 10, 20, 40, 50
# => (10 + 30 + 70 + 120) - 10 = 220
# E.G. 10, 20, 40, 50, 70
# => (10 + 30 + 70 + 120 + 190) - 10 = ...

if __name__ == '__main__':
    _, *nums = map(int, stdin.readlines())
    heapify(nums)
    print(sum(heappush(nums, x := heappop(nums) + heappop(nums)) or x for _ in nums[1:]))
