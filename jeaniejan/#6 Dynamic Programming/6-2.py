#개미전사
n=int(input())
arr=list(map(int,input().split()))
dy=[0]*10000
dy[0]=arr[0]
dy[1]=max(arr[0],arr[1])
for i in range(2,n):
    dy[i]=max(dy[i-1],dy[i-2]+arr[i])
print(dy[n-1])
