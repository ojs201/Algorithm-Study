#1이 될 때까지
n, k = map(int,input().split())
count = 0 # 횟수를 담을 변수
while n != 1:
    
    if n % k == 0 : # 두번째 경우
        n = n // k
        count += 1
    else :
        n -= 1    
        count += 1
print(count)
#샘플이 엄청 큰 수 일때를 고려!

########################
#모범답안
# n, k = map(int, input().split())
# result = 0
 
# while True:
#     target = (n // k) * k
#     result += (n - target)
#     n = target
    
#     if n < k:
#         break
#     result += 1
#     n //= k
    
# result += (n-1)
# print(result)