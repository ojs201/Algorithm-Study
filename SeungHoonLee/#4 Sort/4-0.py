import time
from random import randint
from typing import Callable


class SortTimer:
    """
    정렬 알고리즘 수행 시간 측정기
    """
    items: list[int] = []
    methods: list[Callable[[list[int]], list[int]]] = []

    def __init__(self, methods: list[Callable[[list[int]], list[int]]],
                 size: int = 50_000):
        self.items = [randint(1, 100) for _ in range(size)]
        self.methods = methods

    def measure(self) -> None:
        print(f'\n{f"[Measured time of {len(self.items)} items]":=^50}')

        for method in self.methods:
            start_time: float = time.time()
            method(self.items)
            end_time: float = time.time()
            print(f'{f"{method.__name__}":>25} -> {end_time - start_time}ms')


def selection_sort(items: list[int]) -> list[int]:
    """
    선택 정렬
    """
    n: int = len(items)

    for i in range(0, n):
        min_idx: int = i

        for j in range(i + 1, n):
            if items[min_idx] > items[j]:
                min_idx = j

        items[i], items[min_idx] = items[min_idx], items[i]
    return items


def bubble_sort(items: list[int]) -> list[int]:
    """
    거품 정렬
    """
    n: int = len(items)
    for i in range(0, n):
        for j in range(i + 1, n):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
    return items


def insertion_sort_impl1(items: list[int]) -> list[int]:
    """
    삽입 정렬
    """
    for i in range(1, len(items)):
        next_val: int = items[i]
        j: int = i - 1

        while j >= 0 and items[j] >= next_val:
            items[j + 1] = items[j]
            j = j - 1

        items[j + 1] = next_val
    return items


def insertion_sort_impl2(items: list[int]) -> list[int]:
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j] >= items[j - 1]:
                break
            items[j], items[j - 1] = items[j - 1], items[j]
    return items


def quick_sort_impl1(items: list[int]) -> list[int]:
    """
    퀵 정렬
    분할 과정 [Partition]
    - 피벗(pivot)을 기준으로 두 개의 배열로 분리
    - 왼쪽 배열에서는 피벗보다 큰 데이터 선택
    - 오른쪽 배열에서는 피벗보다 작은 데이터 선택
    - 두 데이터의 위치를 서로 변경
    - 위 과정을 반복하며, 만약 두 데이터의 서로 엇갈리는 경우 피벗과 작은 데이터의 위치를 서로 변경
    """
    partition(items, 0, len(items) - 1)
    return items


def partition(items: list[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot: int = start
    left: int = start + 1
    right: int = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and items[left] <= items[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and items[right] >= items[pivot]:
            right -= 1

        if left > right:  # 엇갈리는 경우 작은 데이터와 피벗을 교환
            items[right], items[pivot] = items[pivot], items[right]
        else:
            items[left], items[right] = items[right], items[left]

    partition(items, start, right - 1)
    partition(items, right + 1, end)


def quick_sort_impl2(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items

    pivot: int = items[0]
    tail: list[int] = items[1:]
    left_side: list[int] = [x for x in tail if x <= pivot]
    right_side: list[int] = [x for x in tail if x > pivot]

    return quick_sort_impl2(left_side) \
        + [pivot] \
        + quick_sort_impl2(right_side)


def count_sort(items: list[int]) -> list[int]:
    """
    계수 정렬
    """
    n: int = max(items) + 1
    nums_count: list[int] = [0] * n

    for item in items:
        nums_count[item] += 1

    answer: list[int] = []

    for i in range(n):
        if nums_count[i] != 0:
            answer += [i for _ in range(nums_count[i])]

    return answer


if __name__ == '__main__':
    timer: SortTimer = SortTimer(methods=[
        selection_sort, bubble_sort,
        insertion_sort_impl1, insertion_sort_impl2,
        quick_sort_impl2,
        count_sort
    ])
    timer.measure()
