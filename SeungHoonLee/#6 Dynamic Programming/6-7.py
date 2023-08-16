"""
6-7. 퇴사
[https://www.acmicpc.net/problem/14501]

풀이:
- 점화식: (D[i] = i번째 날까지 일했을 때 얻을 수 있는 최대 이익)
- i일에 상담 했을 때 받을 수 있는 금액을 P[i], 상담 기간을 T[i]라 할때:
- D[i] = max(D[i], D[i - T[i]] + P[i]) (단, i + T[i] <= N)
"""
from sys import stdin

if __name__ == '__main__':
    N = int(stdin.readline())
    schedule = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
    d = [0] * (N + 1)

    for i in range(N-1, -1, -1):
        t, p = schedule[i]

        if i + t <= N:
            d[i] = max(d[i + 1], d[i + t] + p)
        else:
            d[i] = d[i + 1]

    print(d[0])
