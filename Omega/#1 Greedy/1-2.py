# 큰 수의 법칙

def kth_largest_number(arr, K):
    eigen_nums = set(arr)
    sorted_nums = sorted(eigen_nums, reverse=True)
    return sorted_nums[K-1]

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

largest = kth_largest_number(numbers, 1)
second = kth_largest_number(numbers, 2)

count = k * (m // (k + 1)) + m % (k + 1)
sum = largest * count + second * (m - count)

print(sum)

#다른 풀이
"""
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

largest = kth_largest_number(numbers, 1)
second = kth_largest_number(numbers, 2)

while True:
    for i in range(k):
        if m == 0:
            break
        sum += largest
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1

print(sum)
"""

