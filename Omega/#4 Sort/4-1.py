n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

result = sorted(data, reverse = True)

for i in result:
    print(i, end = ' ')