n = int(input())
arr = input().split()


x = 1
y = 1

for i in arr:
    if i == 'L':
        if y > 1:
            y -= 1
    elif i == 'R':
        if y < n:
            y += 1
    elif i=='U':
        if x > 1:
            x -= 1
    elif i=='D':
        if x < n:
            x += 1

# print(x , y)

# n = int(input())
# moves = input().split()
# x, y = 1, 1
# # L, R, U, D
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# direction = ['L', 'R', 'U', 'D']

# for move in moves: # 입력받은 이동값을 순회
#     for i in range(len(direction)): # 0~3까지 순회
#         # print(len(direction))
#         if move == direction[i]:
#             # nx, ny는 재할당 변수 
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # print(nx, ny)
#     # 예외처리
#     # 조건이 만족하면 계산된 값이 누적되지않고 넘어가게 됨
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         print(nx, ny)
#         continue
#     x, y = nx, ny
    
# print(nx,ny)
