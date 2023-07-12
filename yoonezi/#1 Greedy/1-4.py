n, k = map(int, input().split())

# 횟수
count = 0

while True:
    if n < k: # n이 k보다 작다면 반복문 탈출
            break
    if n % k == 0: # 만약 n이 k로 나눠지면 count 1증가, n은 k로 나눈값으로 변경
        count += 1
        n //= k
        
    else:
        count += 1 #안나눠진다면 1빼고 count 증간
        n -= 1
        
# print(n)
print(count)