# 거스름 돈

N = int(input())
count = 0 # 거슬러줘야 할 동전의 개수

# 500, 100, 50, 10
# 먼저 500원을 최대 몇개 줄 수 있는지
count += (N//500)
N = N % 500
count += (N//100)
N = N % 100
count += (N//50)
N = N % 50
count += (N//10)
N = N % 10

print(count)
####################################
# 모범답안
# N = int(input())
# count = 0

# coin_types = [500, 100, 50, 10]
# for coin in coin_types:
#     count += N//coin
#     N = N % coin
# print(count)