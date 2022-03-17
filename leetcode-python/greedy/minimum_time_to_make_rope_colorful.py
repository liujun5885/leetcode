# https://leetcode-cn.com/problems/minimum-time-to-make-rope-colorful/

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 0
        length = len(colors)
        while i < length:
            max_time = 0
            total_time = 0
            cur = colors[i]

            while i < length and colors[i] == cur:
                max_time = max(neededTime[i], max_time)
                total_time += neededTime[i]
                i += 1

            ans += total_time - max_time

        return ans


import unittest


class TestCases(unittest.TestCase):
    def test_case_01(self):
        colors = "abaac"
        neededTime = [1, 2, 3, 4, 5]
        actual = Solution().minCost(colors, neededTime)
        expected = 3
        self.assertEqual(actual, expected)
