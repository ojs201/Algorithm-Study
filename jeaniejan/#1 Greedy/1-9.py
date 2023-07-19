#볼링공 고르기
n,m=list(map(int,input().split()))
cnt=0
weight=list(map(int,input().split()))

for i in range(n-1):
    for j in range(i+1,n):
        if weight[i]!=weight[j]:
            cnt+=1 
print(cnt)
    
    
    
    