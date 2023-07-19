import math
s=input()
s=list(s)
cnt=0
for i in range(0,len(s)-1):
    if s[i]!=s[i+1]:
        cnt+=1 
<<<<<<< HEAD
print(math.ceil(cnt/2))
=======
print(math.ceil(cnt/2))
>>>>>>> dfdc342a6d56487a7ef2d62b09b165655b96ba18
