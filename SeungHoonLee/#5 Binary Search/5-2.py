"""
5-2. 떡볶이 떡 만들기
관련: 나무 자르기(https://www.acmicpc.net/problem/2805)

문제 풀이:
- 조건에 만족하는 높이의 최대값을 이진 탐색을 통해 찾는 문제
- 높이가 클수록 얻을 수 있는 떡의 길이는 줄어든다.
- 얻을 수 있는 떡의 길이의 합이 필요한 떡의 길이보다 크거나 같을 때까지 반복한다.
- 최적의 높이(H)를 찾을 때까지 다음과 같은 이진 탐색 과정을 수행한다.

1. 주어진 높이(H)에서 중간에 위치한(mid) 높이를 구한다.
2. 1번 과정에서 구한 높이 값으로 주어진 떡들을 자르고, 각 결과를 더한다.
3. 더한 값과 요구된 떡의 길이(M)를 비교한다:

    3-1. 더한 값 > 요구된 떡의 길이(M)
        - 현재 설정한 위치(mid)가 주어진 조건에 만족하는 상태이다.
        - 높이의 최대값을 구하기 위해 탐색 범위를 오른쪽으로 좁혀서 계속 진행한다.

    3-2. 더한 값 < 요구된 떡의 길이(M)
        - 현재 설정한 위치(mid)가 너무 크다.
        - 따라서 탐색 범위를 왼쪽으로 좁혀서 진행한다.

4. 탐색이 끝나면 조건에 만족하는 높이의 최대값을 반환한다.
"""
from sys import stdin


def bin_search(start: int, end: int, target: int) -> int | None:
    if start > end:
        return end

    mid: int = start + ((end - start) // 2)
    total: int = sum([num - mid for num in nums if num > mid])

    if total < target:
        return bin_search(start, mid - 1, target)
    else:
        return bin_search(mid + 1, end, target)


if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))
    print(bin_search(0, 10 ** 9, M))
