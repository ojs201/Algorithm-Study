"""
5-3. 정렬된 배열에서 특정 수의 개수 구하기

- N개의 원소를 포함하는 수열이 오름차 순으로 정렬
- 주어진 X가 수열에 등장하는 횟수를 계산하는 문제
- 이때 시간 복잡도는 O(logN)으로 설계할 것

풀이:
1. 찾고자 하는 요소 X에 대한 개수를 구한다.
2. 총 개수가 0이라면 -1을, 아니라면 구한 개수를 반환한다.
"""
from sys import stdin
from bisect import bisect_left, bisect_right


def count_between(nums: list, el: int) -> int:
    return bisect_right(nums, el) - bisect_left(nums, el)


if __name__ == '__main__':
    N, X = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))
    count = count_between(nums, X)
    print(-1 if count == 0 else count)
