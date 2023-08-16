"""
6-4. 효율적인 화폐 구성

점화식:
- D[N] = 금액 N을 만들 수 있는 최소한의 화폐의 개수
- 각 화폐의 단위 k에 대하여,
    - (N-k)원인 경우가 존재한다면 -> D[N] = min(D[N], D[N-k]) + 1
    - (N-k)원이 존재하지 않는다면 -> D[N] = INF(=10,001)
"""


if __name__ == '__main__':
    n, m = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    INF = 10_001
    d = [INF] * (m + 1)
    d[0] = 0

    for coin in coins:
        for j in range(coin, m + 1):
            if d[j - coin] != INF:
                d[j] = min(d[j], d[j - coin]) + 1

    print(d[m] if d[m] != INF else -1)
