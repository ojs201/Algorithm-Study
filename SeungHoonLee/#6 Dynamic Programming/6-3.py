"""
6-3. 타일 채우기
유사한 문제: 타일 채우기 (https://www.acmicpc.net/problem/2133)

풀이:
- 점화식: D[N] = 2 * D[N-2] + D[N-1]
"""
from sys import stdin


def sol(n):
    if n % 2 == 1:
        return 0

    for i in range(4, n + 1, 2):
        d[i] = (d[i - 2] * d[2])
        d[i] += 2 * sum(d[2:i - 4 + 1:2])
        d[i] += 2

    return d[n]


if __name__ == '__main__':
    N = int(stdin.readline())
    d = [0] * 1_001
    d[1] = 1
    d[2] = 3

    for i in range(3, N + 1):
        d[i] = 2 * d[i - 2] + d[i - 1]

    print(d[N] % 796_796)
