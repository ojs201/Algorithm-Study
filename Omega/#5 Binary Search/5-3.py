# 정렬된 배열에서 특정 수의 개수 구하기
import bisect

n, x = map(int, input().split())
data = list(map(int, input().split()))

sorted(data)
result = bisect.bisect_right(data, x) - bisect.bisect_left(data, x)

print(result)



