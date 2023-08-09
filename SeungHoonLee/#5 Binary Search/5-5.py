"""
5-5. 공유기 설치
https://www.acmicpc.net/problem/2110

입력:
- 집의 개수 N
- 공유기 개수 C
- 집의 좌표 x

출력:
- 가장 인접한 두 공유기 사이의 최대 거리

풀이:
1. 주어진 집 좌표를 정렬한다.
2. 각 집의 좌표 간 거리 값을 구한다.
3. 2번에서 구한 거리 값들을 대상으로 이진 탐색을 수행한다.
    3-1. 중간 거리 값을 구한다.
    3-2. 중간 거리 값을 기준으로 설치 가능한 공유기의 개수를 구한다.
    3-3.
        3-3-1. 설치 가능한 공유기의 개수가 충분한 경우(>=C):
            3-3-1-1. 두 공유기 간 최대 거리를 현재 중간 거리 값으로 설정한다.
            3-3-1-2. 최적의 값을 찾기 위해 오른쪽으로 범위롤 좁혀 탐색을 진행한다.
        3-3-2. 설치 가능한 공유기의 개수가 부족한 경우(< C):
            3-3-2-1. 현재 설정한 거리가 너무 멀기 때문에 공유기를 설치할 수 없다.
            3-3-2-2. 따라서 왼쪽으로 범위를 좁혀 탐색을 진행한다.
4. 최정적으로 구한 최대 거리를 반한한다.
"""
from sys import stdin


def get_number_of_routes(dist):
    nums_routes = 1
    prev = x[0]

    for house in x[1:]:
        if (house - prev) >= dist:
            nums_routes += 1
            prev = house

    return nums_routes


def bin_search(start, end):
    max_dist = 0

    while start <= end:
        dist = (start + end) // 2

        if get_number_of_routes(dist) >= c:
            max_dist = max(max_dist, dist)
            start = dist + 1
        else:
            end = dist - 1

    return max_dist


if __name__ == '__main__':
    n, c = map(int, stdin.readline().strip().split())
    x = list(map(int, stdin.readlines()))
    x.sort()
    print(bin_search(1, x[-1]))
