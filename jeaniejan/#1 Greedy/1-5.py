n=int(input())
a=list(map(int,input().split()))
a.sort()
cnt=0
res=0
for x in a:
    cnt+=1 
    if cnt>=x:
        res+=1 
        cnt=0
print(res)
    