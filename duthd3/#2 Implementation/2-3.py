####### 모범답안
data = input()
x = int(data[1])
y_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = y_list.index(data[0]) + 1

directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
result = 0

for direction in directions:
    dx = x + direction[0]
    dy = y + direction[1]
    
    if(dx >= 1 and dx <=8 and dy>=1 and dy<=8):
        result += 1
print(result)
