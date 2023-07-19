# 음식을 1부터 n까지 반복하면서 음식 섭취 시간을 -1씩, count를 +1씩 계산한다.
# 음식시간이 0이면 넘어가고 마지막 0이될때 종료된다.
# count가 K일때 섭취하는 음식 번호를 출력한다

k = int(input())
food_times = list(map(int, input().split()))

count = 0
result = 0

for i in range(k-1):
    count += 1
    if food_times[i] != 0:
        if k == count:
            result = food_times.index[i]
        else:
            food_times[i]-1
            k += 1
    
print(result)