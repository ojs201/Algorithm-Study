n = int(input())

# 1. 0시 ~ n시
# 2. 00분 ~ 59분
# 3. 00초 ~ 59초

cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                cnt += 1
                
print(cnt)