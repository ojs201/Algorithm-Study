n = input()
# print(n[0], n[1])
x = ord(n[0]) - 96
# print(a)
y = int(n[1])
# print(x, y)
cnt = 0

steps = [(-2,1), (-2,-1), (2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]


for step in steps:
    dx = x + step[0]
    dy = y + step[1]
    if (dx >= 1 and dx <= 8 and dy >= 1 and dy <= 8):
        cnt += 1
        
print(cnt)