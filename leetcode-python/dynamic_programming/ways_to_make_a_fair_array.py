# https://leetcode-cn.com/problems/ways-to-make-a-fair-array/
from itertools import accumulate
from typing import List
from unittest import TestCase


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        dp = [*accumulate(enumerate(nums), lambda r, t: r + (-t[1] if t[0] % 2 else t[1]), initial=0)]
        ans = sum(a + b == dp[-1] for a, b in zip(dp, dp[1:]))
        return ans


class TestCases(TestCase):
    def test_1(self):
        nums = [2, 1, 6, 4]
        expected = 1
        actual = Solution().waysToMakeFair(nums)
        self.assertEqual(expected, actual)
