"""
4-1. 위에서 아래로

- 입력으로 주어진 수열을 내림차순으로 정렬하는 문제
- 정렬된 결과를 공백으로 구분해 출력
- 동일수의 경우 순서 무관
"""
from sys import stdin

items: list[int] = list(map(int, stdin.readlines()))
print(*sorted(items, reverse=True))