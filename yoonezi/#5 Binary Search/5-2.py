n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, result = 0, 0
end = max(arr)

while(start <= end):
    sum = 0
    mid = (start + end) // 2
    for a in arr:
        if a > mid:
            sum += a - mid
    if sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)