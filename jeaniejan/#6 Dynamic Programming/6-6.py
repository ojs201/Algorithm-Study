#정수 삼각형
import sys
input = sys.stdin.readline

#입력
N = int(input())
cost = []
for _ in range(N):
    cost.append([-1]+list(map(int, input().split()))+[-1])

#DP
for i in range(1, N):
    for j in range(1, i+2):
        cost[i][j] += max(cost[i-1][j-1], cost[i-1][j])

print(max(cost[N-1]))