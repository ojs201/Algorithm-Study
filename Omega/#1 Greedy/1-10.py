# 무지의 먹방라이브

# 모범 답안

"""
def solution(food_times, k):
    answer = 0
    index = (k % len(food_times) - 1)

    for i in range(0, k):
        if i % len(food_times) == 0:
            i -= (i / len(food_times)) * len(food_times)
            if food_times[i] == 0:
                continue
            else:
                food_times[i] -= 1
        else:
            if food_times[i] == 0:
                continue
            else:
                food_times[i] -= 1

    while True:
        if food_times[index] == 0:
            break
        else:
            if index == len(food_times) - 1:
                index = 0
            else:
                index += 1

    answer = index + 1

    return answer


import sys

food_times = list(map(int, input().split()))
k = int(sys.stdin.readline().rstrip())
index = (k % len(food_times) - 1)

for i in range(0, k):
    if i > len(food_times) - 1:     # index가 리스트의 길이를 초과하는 경우
        v = (i // len(food_times)) * len(food_times)        # 마지막 연산임을 확인하기 위해 필요한 변수
        i -= (i // len(food_times)) * len(food_times)        # i + v = k라면 마지막 연산이라는 의미
        if food_times[i] == 0:      # 원소가 0이라면 인덱스가 더 큰 가장 가까운 원소 중에 0이 아닌 수를 찾아 1을 뺴는 작업
            while True:
                i += 1
                if i > len(food_times) - 1:
                    break

                if food_times[i] == 0:
                    continue
                else:
                    food_times[i] -= 1
                    break
        else:
            food_times[i] -= 1
    else:
        food_times[i] -= 1

print(food_times)
"""
