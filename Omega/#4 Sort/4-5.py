n = int(input())
data = list(map(int, input().split()))
k = data[-1]
data.sort()
list = []


for i in range(data[0], k + 1):
    sum = 0
    for j in data:
        sum += int(abs(i - j))
    list.append(sum)


print(list.index(min(list)) + 1)