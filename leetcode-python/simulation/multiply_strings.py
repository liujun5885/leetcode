# https://leetcode-cn.com/problems/multiply-strings/

from unittest import TestCase


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = ''
        return ans


class TestCases(TestCase):
    def test_1(self):
        num1 = "2"
        num2 = "3"
        expected = "6"
        actual = Solution().multiply(num1, num2)
        self.assertEqual(actual, expected)

    def test_2(self):
        num1 = "123"
        num2 = "456"
        expected = "56088"
        actual = Solution().multiply(num1, num2)
        self.assertEqual(actual, expected)
