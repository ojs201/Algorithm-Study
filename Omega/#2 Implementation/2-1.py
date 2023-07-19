# 상하좌우

import sys

n = int(sys.stdin.readline().rstrip())
x, y = 1, 1
moving_plan = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moving_types = ['L', 'R', 'U', 'D']

for plan in moving_plan:

    for i in range(len(moving_types)):
        if plan == moving_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)


