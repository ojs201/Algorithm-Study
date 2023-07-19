#게임개발
n,m=map(int,input().split())

d=[[0]*m for _ in range(n)]
x,y,dir=map(int,input().split())
d[x][y]=1

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def t_left():
    global dir
    dir-=1
    if dir==-1:
        dir=3
    
cnt=1
t_time=0
while True:
    t_left()
    nx=x+dx[dir]
    ny=y+dy[dir]
        
    if d[nx][ny]==0 and arr[nx][ny]==0:
        d[nx][ny]=1
        cnt+=1
        t_time=0
        continue
    else:
        t_time+=1
    if t_time==4:
        nx=x-dx[dir]
        ny=y-dy[dir]
        if arr[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        t_time=0
        
print(cnt)
            