"""
5-1. 부품 찾기
"""
from sys import stdin


def bin_search(nums, start, end, target):
    while start <= end:
        mid = start + ((end - start) // 2)

        if nums[mid] == target:
            return 'yes'
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 'no'


if __name__ == '__main__':
    n = int(stdin.readline())
    products = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    orders = list(map(int, stdin.readline().split()))
    products.sort()
    print(*[bin_search(products, 0, n-1, order) for order in orders])
