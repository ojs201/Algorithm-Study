num=input()
res=int(num[0])

for i in range(1,len(num)):
    if int(num[i])<=1 or res<=1:
        res+=int(num[i])
    else:
        res*=int(num[i])

print(res)
