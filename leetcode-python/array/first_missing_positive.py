# https://leetcode-cn.com/problems/first-missing-positive/

from typing import List
from unittest import TestCase


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                x, y = i, nums[i] - 1
                nums[x], nums[y] = nums[y], nums[x]

        for i in range(n):
            if i != nums[i] - 1:
                return i + 1

        return n + 1


class TestCases(TestCase):
    def test_1(self):
        nums = [3, 4, -1, 1]
        expected = 2
        actual = Solution().firstMissingPositive(nums)
        self.assertEqual(expected, actual)
