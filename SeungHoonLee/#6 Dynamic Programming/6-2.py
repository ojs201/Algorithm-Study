"""
6-2. 개미 전사

풀이:
- 점화식: D[N] = max(D[N-1], D[N-2] + foods[N])
    - D[N] = N번째 창고까지 얻을 수 있는 식량의 최대값
    - foods[N] = N번째 창고에 저장된 식량의 개수
"""


if __name__ == '__main__':
    N = int(input())
    foods = list(map(int, input().split()))
    d = [0] * N
    d[0] = 0
    d[1] = max(foods[0], foods[1])

    for i in range(3, N):
        d[i] = max(d[i-1], d[i-2] + foods[i])

    print(d[N-1])
