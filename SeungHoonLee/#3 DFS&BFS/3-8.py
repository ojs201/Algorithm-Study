"""
3-8. 감시 피하기
https://www.acmicpc.net/problem/18428

풀이:
복도에 설치 가능한 빈칸 위치를 기준으로 완전탐색(DFS)을 진행한다.

- 복도에서 빈칸(X)을 탐색한다.
- 해당 위치에 임의로 장애물(O)을 설치한다.
- 장애물을 모두 설치하였을 때, 학생을 탐지하지 못하는 경우가 존재한다면 "YES",
  어느 경우도 존재하지 않으면 "NO"를 출력한다.
"""
from sys import stdin

TEACHER: str = 'T'
STUDENT: str = 'S'
OBSTACLE: str = 'O'
EMPTY: str = 'X'


def dfs(nums_obstacle: int) -> bool:
    global ans

    if nums_obstacle == 3:
        return not find_students()
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == EMPTY:
                    graph[i][j] = OBSTACLE

                    if dfs(nums_obstacle + 1):
                        ans = 'YES'
                        return True

                    graph[i][j] = EMPTY


def find_students() -> bool:
    for x, y in teachers:
        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if find_student(x, y, *direction):
                return True
    return False


def find_student(x: int, y: int, dir_x: int, dir_y: int) -> bool:
    while True:
        x += dir_x
        y += dir_y

        # 경계 검사
        if 0 > x or x > N - 1 or 0 > y or y > N - 1:
            break

        # 장애물을 만날 경우
        if graph[x][y] == OBSTACLE or graph[x][y] == TEACHER:
            break

        # 학생을 찾을 경우
        if graph[x][y] == STUDENT:
            return True

    return False


if __name__ == '__main__':
    N: int = int(stdin.readline().rstrip())
    graph: list[list[str]] = []
    teachers: list[tuple] = []
    ans: str = 'NO'

    for i in range(N):
        graph.append(list(stdin.readline().rstrip().split()))

        for j in range(N):
            if graph[i][j] == TEACHER:
                teachers.append((i, j))

    dfs(0)
    print(ans)
