# https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique/

import unittest
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        c_counter = Counter(s)

        sorted_frequency = sorted(c_counter.values(), reverse=True)
        for i in range(1, len(sorted_frequency)):
            if sorted_frequency[i] >= sorted_frequency[i - 1]:
                freq = sorted_frequency[i]
                sorted_frequency[i] = max(0, sorted_frequency[i - 1] - 1)
                ans += freq - sorted_frequency[i]
        return ans


class TestCases(unittest.TestCase):
    def test_01(self):
        s = 'aab'
        expected = 0
        actual = Solution().minDeletions(s)
        self.assertEqual(actual, expected)

    def test_02(self):
        s = 'aaabbbcc'
        expected = 2
        actual = Solution().minDeletions(s)
        self.assertEqual(actual, expected)

    def test_03(self):
        s = "abcabc"
        expected = 3
        actual = Solution().minDeletions(s)
        self.assertEqual(actual, expected)

    def test_04(self):
        s = "bbcebab"
        expected = 2
        actual = Solution().minDeletions(s)
        self.assertEqual(actual, expected)
