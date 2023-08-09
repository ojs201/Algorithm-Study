"""
4-3. 두 배열의 원소 교체

- N -> (배열의 원소 개수), K -> (최대 교체 횟수)
- 배열 A와 B가 주어졌을 때, 최대 K번의 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최대값을 구하는 문제
- 1<= N <= 100,000
- 0 <= K <= N
= 배열 A와 B의 모든 원소는 10,000,000 보다 작은 자연수이다.
"""
from sys import stdin

lines: list[str] = stdin.readlines()

N, K = map(int, lines[0].split())
A, B = map(
    lambda x: list(map(int, x.strip().split())),
    lines[1:]
)

A = sorted(A)
B = sorted(B, reverse=True)
print(sum([max(A[i], B[i]) for i in range(K)] + A[K:]))