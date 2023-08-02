#국영수
n=int(input())
list=[]
for i in range(n):
    [name,kor,eng,math]=map(str,input().split())
    list.append([name,int(kor),int(eng),int(math)])
list.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in list:
    print(i[0])
