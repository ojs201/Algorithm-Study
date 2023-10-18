n = int(input())
arr = []
min = 100
for i in range(n):
    a, b = input().split()
    info = (b, a)
    arr.append(info)

arr.sort()
for i in range(n):
    print(arr[i][1], end= " ")   
 