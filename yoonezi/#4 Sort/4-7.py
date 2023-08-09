# 10 20 40 
# 30
# 70
# 100

# 50
# 50 20 70
# 120

# 60
# 60 10 70
# 130

# --------------------
# 40 60 70
# 100
# 100 70 170
# 270

# 130
# 130 40 170
# 300

# 110
# 110 60 170
# 280
# -------------------
# 결론 : 오름차순 한 다음에 제일 작은거 두개 더하고 , 여기에 계속 더해가는 방식이 최소값 

import heapq

n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# # print(arr)
# arr.sort()
# # print(arr)
# sum = 0
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))
if len(card) == 1:
    print(0)
else:
    sum = 0
    while len(card) > 1:
        tmp1 = heapq.heappop(card)
        tmp2 = heapq.heappop(card)
        sum += tmp1+tmp2
        heapq.heappush(card, tmp1+tmp2)
    print(sum)