# 럭키 스트레이트

n = list(map(int, input()))
p = len(n) // 2
sum1 = 0
sum2 = 0

for i in range(0, p):
    sum1 += n[i]

for i in range(p, len(n)):
    sum2 += n[i]

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')