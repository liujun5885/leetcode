# https://leetcode-cn.com/problems/largest-perimeter-triangle/

from typing import List
from unittest import TestCase


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums, reverse=True)
        ans = 0

        if n < 3:
            return 0

        for i in range(n - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                ans = max(ans, nums[i] + nums[i + 1] + nums[i + 2])

        return ans


class TestCases(TestCase):
    def test_1(self):
        nums = [2, 1, 2]
        expected = 5
        actual = Solution().largestPerimeter(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1, 2, 1]
        expected = 0
        actual = Solution().largestPerimeter(nums)
        self.assertEqual(expected, actual)
