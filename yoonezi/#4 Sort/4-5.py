# 제한 시간 1초 > 이중포문 x

n = int(input())
home = list(map(int, input().split()))
home.sort()
print(home[(n-1)//2])
    