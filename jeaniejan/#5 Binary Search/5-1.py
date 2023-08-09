#부품찾기

def func(arr,left,right,target):
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        elif arr[mid]>target:
            right=mid-1
    return None
    
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
        
for i in b:
    x=func(a,0,n-1,i)
    if x!=None:
        print('yes',end=' ')
    else:
        print('no',end=' ')



func(n,a,m,b)
