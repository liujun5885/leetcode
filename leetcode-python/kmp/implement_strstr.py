# https://leetcode-cn.com/problems/implement-strstr/

from unittest import TestCase


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return -1


class TestCases(TestCase):
    def test_1(self):
        haystack = "hello"
        needle = "ll"
        expected = 2
        actual = Solution().strStr(haystack, needle)
        self.assertEqual(expected, actual)

    def test_2(self):
        haystack = "aaaaa"
        needle = "bba"
        expected = -1
        actual = Solution().strStr(haystack, needle)
        self.assertEqual(expected, actual)
