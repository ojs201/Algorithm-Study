from unittest import TestCase
from converter import BracketConverter


class TestBracketConverter(TestCase):
    def setUp(self) -> None:
        self.converter = BracketConverter()

    def test_is_correct(self):
        """올바른 괄호 문자열 검증"""
        self.assertTrue(self.converter.is_correct('(()())()'))
        self.assertTrue(self.converter.is_correct('()'))
        self.assertTrue(self.converter.is_correct('()(())()'))
        self.assertFalse(self.converter.is_correct('(()))('))

    def test_split_uv(self):
        """u, v 괄호 문자열 분리"""
        self.assertEqual((')(', ''), self.converter.split_uv(')('))
        self.assertEqual(('()', '))((()'), self.converter.split_uv('()))((()'))
        self.assertEqual(('))((', '()'), self.converter.split_uv('))((()'))

    def test_reverse_brackets(self):
        """괄호 방향 반전"""
        self.assertEqual('))()(()(', self.converter.reverse_brackets('(()())()'))
        self.assertEqual('', self.converter.reverse_brackets(''))
        self.assertEqual('()', self.converter.reverse_brackets(')('))
        self.assertEqual('(())', self.converter.reverse_brackets('))(('))

    def test_convert(self):
        """문자열 변환"""
        self.assertEqual('(()())()', self.converter.convert('(()())()'))
        self.assertEqual('()', self.converter.convert(')('))
        self.assertEqual('()(())()', self.converter.convert('()))((()'))
