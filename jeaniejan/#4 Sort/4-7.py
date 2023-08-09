#카드 정렬하기
import heapq

n = int(input())

heap = []
for i in range(n) :
  data = int(input())
  heapq.heappush(heap, data)

result = 0

while len(heap) != 1 :
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)

  sum_value = a + b
  result += sum_value
  heapq.heappush(heap, sum_value)

print(result)