"""
3-9. 인구이동
https://www.acmicpc.net/problem/16234

풀이:
- 주어진 도시들을 모두 순회하면서 다음 로직을 수행한다.
- 현재 도시를 시작으로 완전 탐색(DFS)으로 연합 도시들을 탐색한다.
- 연합 도시들이 존재하는 경우, 인구 이동을 수행한다.
- 만약 주어진 도시들에 대한 모든 순회가 끝났을 때, 연합을 맺을 도시가 종료하지 않는 경우 탐색을 종료한다.
"""
from sys import stdin
from collections import deque


def find_unions(i: int, j: int) -> list[tuple]:
    unions: list[tuple] = [(i, j)]
    q: deque = deque()
    q.append((i, j))

    while q:
        for x, y in find_unions_of(*q.popleft()):
            if not visited[x][y]:
                visited[x][y] = True
                unions.append((x, y))
                q.append((x, y))
    return unions


def find_unions_of(i: int, j: int) -> list[tuple]:
    unions: list[tuple] = [(i, j)]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = i + dx, j + dy

        if (0 > x or x >= N or 0 > y or y >= N) or visited[x][y]:
            continue

        if L <= abs(A[x][y] - A[i][j]) <= R:
            unions.append((x, y))
    return unions


if __name__ == '__main__':
    N, L, R = map(int, stdin.readline().split())
    A = [list(map(int, stdin.readline().split())) for _ in range(N)]
    days_migrates: int = 0

    while True:
        visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
        exist_union: bool = False

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    unions: list[tuple] = find_unions(i, j)

                    if (size := len(unions)) > 1:
                        exist_union = True
                        avg_popul = sum([A[x][y] for x, y in unions]) // size

                        for x, y in unions:
                            A[x][y] = avg_popul

        if not exist_union:
            break

        days_migrates += 1

    print(days_migrates)
