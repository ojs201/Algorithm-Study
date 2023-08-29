#공유기 설치
def Count(len):
    cnt=1
    ep=arr[0]
    for i in range(1,n):
        if arr[i]-ep>=len:
            cnt+=1
            ep=arr[i]
    return cnt

n,c=map(int,input().split())
arr=[]

for _ in range(n):
    tmp=int(input())
    arr.append(tmp)
arr.sort()
lt=1
rt=arr[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)