"""
3-7. 연산자 끼워넣기
https://www.acmicpc.net/problem/14888

무엇이 다른가?
- 이전 풀이 방법에서는 '연산자'만을 대상으로 dfs를 수행함.
- 이 방식은 '연산자' 뿐만 아니라 '피연산자'를 포함하여 계산한 경우의 수를 구하는 방식
- 연산자 순열 집합을 구하고, 이에 대한 합을 각각 구하지 않고 한번에 계산하므로 수행 시간이 훨신 빠름
- 이전[592ms] -> 이후[56ms]
"""
from sys import stdin


def dfs(prev_v: int, idx: int, plus, minus, mutiply, divide):
    if idx == N:
        res.append(prev_v)
    else:
        if plus:
            dfs(prev_v + A[idx], idx + 1, plus - 1, minus, mutiply, divide)
        if minus:
            dfs(prev_v - A[idx], idx + 1, plus, minus - 1, mutiply, divide)
        if mutiply:
            dfs(prev_v * A[idx], idx + 1, plus, minus, mutiply - 1, divide)
        if divide:
            next_v: int = abs(prev_v) // A[idx] * -1 if prev_v < 0 else prev_v // A[idx]
            dfs(next_v, idx + 1, plus, minus, mutiply, divide - 1)


if __name__ == '__main__':
    N: int = int(stdin.readline())
    A: list[int] = list(map(int, stdin.readline().split()))
    ops: list[int] = list(map(int, stdin.readline().split()))
    res = []

    dfs(A[0], 1, *ops)
    print(max(res), min(res), sep='\n')
