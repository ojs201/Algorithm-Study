#문자열 재정렬
s=input()
res=0
list=[]
for x in s:
    if x.isdecimal():
        res+=int(x)
    else:
        list.append(x)
        list=sorted(list)
for i in range(len(list)):
    print(list[i],end='')
print(res)