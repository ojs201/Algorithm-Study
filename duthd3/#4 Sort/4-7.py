import heapq

n = int(input())
result = 0
arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))

print(arr)

    
for i in range(n-1):
    prev = heapq.heappop(arr)
    cur = heapq.heappop(arr)
    
    result += prev + cur
    heapq.heappush(arr, prev + cur)

print(result)