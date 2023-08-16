"""
6-6. 정수 삼각형

풀이:
- 점화식: D[i][j]: 삼각형의 (i, j) 요소부터 (0, 0)까지 최대가 되는 경로에 있는 수의 합
- D[i][j] = triangle[i][j] + max(D[i-1][j-1], D[i-1][j])
"""

if __name__ == '__main__':
    H = int(input())
    triangle = []

    for _ in range(H):
        triangle.append(list(map(int, input().split())))

    d = triangle.copy()

    for i in range(H - 1, -1, -1):
        for j in range(0, i):
            d[i-1][j] += max(d[i][j], d[i][j+1])

    print(d[0][0])
