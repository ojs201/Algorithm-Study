#고정점 찾기
n=int(input())
arr=list(map(int,input().split()))
lt=0
rt=n-1
def binarySearch(array,left,right):
    while left<=right:
        mid=(left+right)//2
        if array[mid]==mid:
            return mid
        elif array[mid]>mid:
            right=mid-1
        elif array[mid]<mid:
            left=mid+1 
    return mid-1
    
res=binarySearch(arr,lt,rt)
print(res)