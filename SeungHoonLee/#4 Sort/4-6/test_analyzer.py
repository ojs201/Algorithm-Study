from unittest import TestCase
from analyzer import FailureRateAnalyzer


class TestFailureRateAnalyzer(TestCase):

    def test_analyze(self):
        """실패율 테스트"""
        analyzer = FailureRateAnalyzer(5, [2, 1, 2, 6, 2, 4, 3, 3])
        self.assertEqual([3, 4, 2, 1, 5], analyzer.analyze())

        analyzer = FailureRateAnalyzer(4, [4, 4, 4, 4, 4])
        self.assertEqual([4, 1, 2, 3], analyzer.analyze())