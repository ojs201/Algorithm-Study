# 카드 정렬하기
# 출력초과???
import sys

n = int(sys.stdin.readline().rstrip())
data = []
result = 0

for i in range(n):
    inp = int(sys.stdin.readline().rstrip())
    data.append(inp)

data.sort()

temp = data[0]
for i in range(n - 1):
    result += (temp + data[i + 1])
    temp = result

print(result)

