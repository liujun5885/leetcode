# https://leetcode-cn.com/problems/alien-dictionary/

from typing import List
from unittest import TestCase


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        return ""


class TestCases(TestCase):
    def test_1(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        expected = "wertf"
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)

    def test_2(self):
        words = ["z", "x"]
        expected = "zx"
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)

    def test_3(self):
        words = ["z", "x", "z"]
        expected = ""
        actual = Solution().alienOrder(words)
        self.assertEqual(actual, expected)
