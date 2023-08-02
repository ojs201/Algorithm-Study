"""
3-10. 블록 이동하기
"""
from collections import deque


def generate_next_pos(pos: set[tuple],
                      board: list[list[int]]) -> list[set[tuple]]:

    pos: list[tuple] = list(pos)
    next_pos: list[set[tuple]] = []

    (x1, y1), (x2, y2) = pos[0], pos[1]

    # 상하좌우 이동 경로 탐색
    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dx, dy = direction
        next_x1, next_y1 = x1 + dx, y1 + dy
        next_x2, next_y2 = x2 + dx, y2 + dy

        if is_empty(board[next_x1][next_y1], board[next_x2][next_y2]):
            next_pos.append({(next_x1, next_y1), (next_x2, next_y2)})

    # 가로/세로 방향에 따른 회전 경로 탐색
    if pos[0][0] == pos[1][0]:
        for offset in [1, -1]:
            dx1, dx2 = x1 + offset, x2 + offset

            if is_empty(board[dx1][y1], board[dx2][y2]):
                next_pos.append({(x1, y1), (dx1, y1)})
                next_pos.append({(x2, y2), (dx2, y2)})
    else:
        for offset in [1, -1]:
            dy1, dy2 = y1 + offset, y2 + offset

            if is_empty(board[x1][dy1], board[x2][dy2]):
                next_pos.append({(x1, y1), (x1, dy1)})
                next_pos.append({(x2, y2), (x2, dy2)})

    return next_pos


def is_empty(pos1: int, pos2: int):
    return pos1 == 0 and pos2 == 0


def solution(board: list[list[int]]):
    n: int = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    visited: list[set[tuple]] = []
    pos: set[tuple] = {(1, 1), (1, 2)}
    q: deque = deque()
    cost: int = 0

    q.append((pos, cost))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()

        if (n, n) in pos:
            return cost

        for next_pos in generate_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0


if __name__ == '__main__':
    print(solution([
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]))
