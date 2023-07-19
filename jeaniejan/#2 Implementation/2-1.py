#상하좌우
n=int(input())
plan=list(map(str,input().split()))
dx=[0,0,-1,1]
dy=[-1,1,0,0]
x,y=1,1
move=['L','R','U','D']

for k in plan:
    if k==move[0]:
        if y==1:
            continue
        x=x+dx[0]
        y=y+dy[0]

    if k==move[1]:
        if y==5:
            continue
        x=x+dx[1]
        y=y+dy[1]

    if k==move[2]:
        if x==1:
            continue
        x=x+dx[2]
        y=y+dy[2]

    if k==move[3]:
        if x==5:
            continue
        x=x+dx[3]
        y=y+dy[3]

print(x,y)