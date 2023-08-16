"""
6-8. 병사 배치하기
[https://www.acmicpc.net/problem/18353]
"""
from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split()))
    dp = [1] * n

    nums.reverse()

    for i in range(1, n):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(n - max(dp))
