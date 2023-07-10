# 큰 수의 법칙
N, M, K = map(int, input().split())
count = 0 # 결과값 담을 변수
limit_count = 0 # 몇 번 더했는지를 담을 변수

array = list(map(int, input().split()))
array.sort()
print(array)
#M번 더하여 가장 큰 수, 연속해서 K번 초과 X
for i in range(M):
    if limit_count >=K:
        count += array[N-2]
        limit_count = 0
    else:
        count += array[N-1]
        limit_count += 1

print(count)

#######################
#모범답안
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()

# first = data[n-1]
# second = data[n-2]

# result = 0

# while True:
#     for i in range(k): # 가장 큰 수 k번 만큼 더하기
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1 

# print(result)