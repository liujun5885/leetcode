# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = b2 = -prices[0]
        s1 = s2 = 0
        for p in prices:
            b1 = max(b1, -p)
            s1 = max(s1, b1 + p)
            b2 = max(b2, s1 - p)
            s2 = max(s2, b2 + p)

        return s2


class TestCases(TestCase):
    def test_1(self):
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expected = 6
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_2(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_3(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_4(self):
        prices = [1]
        expected = 0
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)
