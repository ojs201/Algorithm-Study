"""
6-1
관련: 1로 만들기 (https://www.acmicpc.net/problem/1463)

- 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
    - X가 5으로 나누어 떨어지면, 5으로 나눈다.
    - X가 3으로 나누어 떨어지면, 3으로 나눈다.
    - X가 2로 나누어 떨어지면, 2로 나눈다.
    - 1을 뺀다.
- 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
- 연산을 사용하는 횟수의 최솟값을 출력하시오.

풀이:
- 점화식:
    - D[N] = min(D[N-1], D[N//2], D[N//3]) + 1
    - D[N] -> 정수 N에 대한 연산 횟수의 최솟값
"""
from sys import stdin


def sol(num):
    d = [0] * (num + 1)

    for i in range(2, num + 1):
        d[i] = d[i - 1] + 1

        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)

        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)

    return d[num]


if __name__ == '__main__':
    N = int(stdin.readline())
    print(sol(N))
