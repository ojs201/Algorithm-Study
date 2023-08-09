"""
5-4. 고정점
"""
from sys import stdin


def bin_search(nums, start, end):
    while start <= end:
        mid = start + ((end - start) // 2)

        if nums[mid] == mid:
            return mid
        elif nums[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1

    return None


if __name__ == '__main__':
    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))

    if (fixed_point := bin_search(nums, 0, n - 1)) is None:
        print(-1)
    else:
        print(fixed_point)
