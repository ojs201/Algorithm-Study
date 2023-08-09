# 전형적인 이진탐색?
n = int(input())

arr = list(map(int, input().split()))

def b_search(arr, s, e):
    if s > e:
        return '-1' #고정점이 존재하지 않는다면 -1
    mid = (s + e) // 2
    if arr[mid] == mid : #mid와 arr[mid]값이 동일할 경우 고정점
        return mid
    elif arr[mid] < mid :
        return b_search(arr, mid+1, e)
    else:
        return b_search(arr, s, mid-1)

result = b_search(arr, 0, n-1)
print(result)    