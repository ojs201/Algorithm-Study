"""
4-5. 안테나

집의 수 N이 주어졌을 때, 안테나를 기준으로 모든 집까지의 거리의 총합이 최소가 되게 하는 위치를
구해야 함

- 안테나는 특정 위치의 집에 설치됨
- 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치
    - 이때 동일한 위치에 여러 집이 존재하는 경우도 가능
- 안테나를 설치할 수 있는 위치 값으로 여러 개의 값이 도출되는 경우 가장 작은 값을 출력

e.g. N = 4, houses = [5, 1, 7, 9]
1. 5에 설치하는 경우: (0 + 4 + 2 + 4) = 10
2. 1에 설치하는 경우: (4 + 0 + 6 + 8) = 18
3. 7에 설치하는 경우: (2 + 6 + 0 + 2) = 10
4. 9에 설치하는 경우: (4 + 8 + 2 + 0) = 14

> 이때 거리의 총합이 최소가 되는 위치는 '5' 또는 '7'
> 두 수 중 가장 작은 값을 출력해야 하므로 답읍 '5'

문제 풀이 전략 [1/2] (시간초과)
1. 각 집 위치를 기준으로 거리의 총합을 구한다.
2. 거리의 총합의 최소값을 가지는 위치를 구한다.
3. 해당하는 수들 중 최소값을 구한다.

문제 풀이 전략 [2/2]
안테나를 기준으로 각 거리의 총합의 초소값은 중간값이 될 수 밖에 없다.
따라서 주어진 집을 오름차 순으로 정렬시키고 중값값을 출력한다.
"""
from sys import stdin

N = int(stdin.readline())
dists = set(map(int, stdin.readline().split()))
print(sorted(dists)[(N - 1) // 2])

# dists = []
# for h_dist in h_dists:
#     dist = sum([abs(curr_dist - h_dist) for curr_dist in h_dists])
#     dists.append([h_dist, dist])
#
# dists = sorted(dists, key=lambda d: (d[1], d[0]))
# print(dists[0][0])