# 만들 수 없는 금액

import sys

# k번째 최댓값을 구하는 함수
def kth_largest_number(arr, K):
    eigen_nums = set(arr)
    sorted_nums = sorted(eigen_nums, reverse=True)
    return sorted_nums[K - 1]


n = int(sys.stdin.readline().rstrip())
data = list(map(int, input().split()))
sum = 0
data.sort()

for i in range(0, len(data)):
    sum += data[i]

if data[0] > 1:  # 최솟값 > 1 이라면 1 출력
    print('1')

elif kth_largest_number(data, 1) > sum - kth_largest_number(data, 1):  # 가장 큰 수 > 나머지 합인 경우
    print(sum - kth_largest_number(data, 1) + 1)

else:  # n번째로 큰 수 > 나머지 합인 경우
    minus = kth_largest_number(data, 1)
    for i in range(2, len(data) - 1):
        minus += kth_largest_number(data, i)  # 최댓값 + 2번째 최댓값 + ... + i번째 최댓값을 구하기 위한 변수
        if kth_largest_number(data, i) > sum - minus:  #
            print(sum - minus + 1)  # 전체합 - 변수(1번쨰, 2번쨰, ... i번째로 큰 값을 더한 값) + 1
            break
        else:
            continue
