# data_num = int(input())
# data_str = input().split()
# x=1
# y=1

# length = len(data_str)
# for i in data_str:
#     if i == "R":
#         if y<data_num:
#             y += 1
#     elif i == "L":
#         if y>1:
#             y -= 1
#     elif i =="U":
#         if x > 1:
#             x -= 1
#     else:
#         if x < data_num:
#             x += 1
# print(x, y)

################################################
#모범답안
n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1] # L R U D
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나면 무시한다
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny

print(x, y)