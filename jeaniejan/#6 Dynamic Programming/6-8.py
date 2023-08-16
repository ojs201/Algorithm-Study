#병사 배치하기
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i): # 0 <= j < i 
        if a[i] < a[j]: # 내림차순이기 때문에
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp)) # n - 가장 긴 내림차순 부분 수열의 길이 