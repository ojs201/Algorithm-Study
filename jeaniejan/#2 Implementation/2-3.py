s=input()
for x in s:
    if x.isdecimal():
        num=int(x)
    else:
        alpha=x

dir=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
res=0
for x in dir:
    row=num+x[0]
    col=ord(alpha)-ord('a')+1+x[1]
    if row>=1 and row<=8 and col>=1 and col<=8:
        res+=1
print(res)