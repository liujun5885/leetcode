# https://leetcode-cn.com/problems/longest-arithmetic-subsequence/

from typing import List
from unittest import TestCase
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 0
        dp = defaultdict(lambda: defaultdict(int))
        n = len(nums)
        if n <= 2:
            return 1

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = max(dp[j][diff] + 1, dp[i][diff])
                ans = max(ans, dp[i][diff])

        return ans + 1


class TestCases(TestCase):
    def test_1(self):
        nums = [3, 6, 9, 12]
        expected = 4
        actual = Solution().longestArithSeqLength(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [9, 4, 7, 2, 10]
        expected = 3
        actual = Solution().longestArithSeqLength(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [20, 1, 15, 3, 10, 5, 8]
        expected = 4
        actual = Solution().longestArithSeqLength(nums)
        self.assertEqual(expected, actual)
