# 왕실의 나이트

now = input()
row = int(ord(now[0])) - 96
col = int(now[1])
s_row, s_col = row, col
count = 0
dx = [1,2,-1,2,1,-2,1,-2]
dy = [2,1,2,-1,-2,-1,-2,1]

for i in range(8):
    row = s_row
    col = s_col
    row += dx[i]
    col += dy[i]
    if row < 1 or col < 1 or row > 8 or col > 8:
        continue
    else:
        count += 1

print(count)


