n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(reverse=True)
for i in arr:
    print(i, end=' ')