#떡 자르기
n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))

start, end = 0, max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1 
    else:
        result = mid
        start = mid + 1

print(result)