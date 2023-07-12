# 숫자 카드 게임

n, m = map(int, input().split())
min_value = []
for i in range(n):
    value = list(map(int, input().split()))
    min_value.append(min(value))

result = max(min_value)

print(result)
