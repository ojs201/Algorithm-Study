"""
4-7. 카드 정렬하기
https://www.acmicpc.net/problem/1715

풀이:
1. 주어진 숫자를 오름차 순으로 정렬한다.
2. 정렬된 숫자들을 2개씩 뽑아 더한다.
3. 이후 남은 집합에 대해 동일한 연산을 수행한다.
"""
from sys import stdin
from heapq import heapify, heappush, heappop

if __name__ == '__main__':
    _, *nums = map(int, stdin.readlines())
    heapify(nums)
    print(sum(heappush(nums, x := heappop(nums) + heappop(nums)) or x for _ in nums[1:]))
