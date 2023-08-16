"""
6-5. 금광

풀이:
- 점화식: D[i][j] = (i, j)까지 얻을 수 있는 최대 금의 크기
- (i, j)에 대응되는 금의 크기 golds[i][j]에 대하여
- D[i][j] = golds[i][j] + max(D[i-1][j-1], D[i][j-1] + D[i+1][j-1])
"""

if __name__ == '__main__':
    for i in range(int(input())):
        n, m = map(int, input().split())
        g = list(map(int, input().split()))

        golds = [g[i:i + m] for i in range(0, n * m, m)]
        d = [[0 for _ in range(m)] for _ in range(n)]
        ans = 0

        for i in range(n):
            d[i][0] = golds[i][0]

        for j in range(0, m):
            for i in range(1, n):
                left = d[i][j - 1]
                left_up = d[i - 1][j - 1] if i > 0 else 0
                left_down = d[i + 1][j - 1] if i + 1 < n else 0
                d[i][j] = golds[i][j] + max(left_up, left, left_down)

        for i in range(n):
            ans = max(ans, d[i][m-1])

        print(ans)
