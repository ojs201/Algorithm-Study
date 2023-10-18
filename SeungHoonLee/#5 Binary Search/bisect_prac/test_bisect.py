from unittest import TestCase
from bisect import bisect_left, bisect_right


def count_between(nums: list, left: int, right: int) -> int:
    """
    count number of elements between `left` and `right`.
    """
    return bisect_right(nums, right) - bisect_left(nums, left)


class Test(TestCase):

    def setUp(self) -> None:
        self.nums = [1, 2, 4, 4, 8]

    def test_bisect_left(self):
        """bisect_left 기능 테스트"""
        self.assertEqual(2, bisect_left(self.nums, 4))

    def test_bisect_right(self):
        """bisect_right 기능 테스트"""
        self.assertEqual(4, bisect_right(self.nums, 4))

    def test_count_between(self):
        """count_between 기능 테스트"""
        self.assertEqual(2, count_between(self.nums, 4, 4))
        self.assertEqual(4, count_between(self.nums, 1, 4))
        self.assertEqual(3, count_between(self.nums, 4, 8))
        self.assertEqual(len(self.nums), count_between(self.nums, -1, 8))
