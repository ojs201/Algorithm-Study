from unittest import TestCase
from lyrics_finder import LyricsFinder, count_between


class TestLyricsFinder(TestCase):
    def setUp(self) -> None:
        self.words = sorted(["frodo", "front", "frost", "frozen", "frame", "kakao"])
        self.finder = LyricsFinder(self.words)

    def test_count_between(self):
        """
        단어 수 세기 검증
        """
        # ????? ~ ?????? -> ALL
        count = count_between(self.words, "a", "z")
        self.assertEqual(6, count)

        # 'ka???' -> kakao
        count = count_between(self.words, "kaaaa", "kazzz")
        self.assertEqual(1, count)

        # 'fra??' -> ["frame"]
        count = count_between(self.words, "fraaa", "frazz")
        self.assertEqual(1, count)

        # 'fro??' -> ["frodo", "front", "frost", "frozen"]
        count = count_between(self.words, "froaa", "frozz")
        self.assertEqual(4, count)

        # 'fr???' -> ["frodo", "front", "frost", "frozen", "frame"]
        count = count_between(self.words, "fraaa", "frzzz")
        self.assertEqual(5, count)

        # 'fro???' -> ["frodo", "front", "frost", "frozen"]
        count = count_between(self.words, "froaaa", "frozzz")
        self.assertEqual(4, count)

        # 'pro?' -> []
        count = count_between(self.words, "proa", "proz")
        self.assertEqual(0, count)

        # '????o' -> ['kakao']
        count = count_between(['oakak'], "oaaaa", "obbbb")
        self.assertEqual(1, count)

        # '???zen' -> ['frozen']
        count = count_between(['nezorf'], "nezaaa", "nezzzz")
        self.assertEqual(1, count)

        # '????t' -> ["front", "frost"]
        count = count_between(['tnorf', 'tsorf'], "taaaa", "tzzzzz")
        self.assertEqual(2, count)

    def test_execute_query(self):
        """
        쿼리 매칭 테스트
        """
        self.assertEqual(3, self.finder.execute_query("fro??"))
        self.assertEqual(2, self.finder.execute_query("????o"))
        self.assertEqual(4, self.finder.execute_query("fr???"))
        self.assertEqual(1, self.finder.execute_query("fro???"))
        self.assertEqual(0, self.finder.execute_query("pro?"))
