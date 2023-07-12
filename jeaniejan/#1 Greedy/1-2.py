n,m,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
res=0
while True:
    for _ in range(k):
        if m==0:
            break
        res+=a[0]
        m-=1 
    if m==0:
        break
    res+=a[1]
    m-=1
print(res)