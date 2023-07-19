

n, m = map(int, input().split())
weight = list(map(int, input().split()))

result = 0
# 마지막 번호까지 구할 필요 없으니 n-1까지 반복
for i in range(n-1):
    for j in range(i+1, n):
        if weight[i] != weight[j]:
            result +=1
            
print(result)
            