n,m=map(int,input().split())
arr= []
max=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    arr[i].sort()
for i in range(n):
        if arr[i][0]>max:
            max=arr[i][0]
print(max)