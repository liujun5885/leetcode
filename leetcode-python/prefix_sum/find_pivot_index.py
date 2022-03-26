# https://leetcode-cn.com/problems/find-pivot-index/
from typing import List
from unittest import TestCase


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        pre_sum = [0 for _ in range(len(nums) + 1)]

        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            total += nums[i - 1]

        for i in range(len(nums)):
            if pre_sum[i] == total - pre_sum[i] - nums[i]:
                return i

        return -1


class TestCases(TestCase):
    def test_1(self):
        nums = [1, 7, 3, 6, 5, 6]
        expected = 3
        actual = Solution().pivotIndex(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1, 2, 3]
        expected = -1
        actual = Solution().pivotIndex(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [2, 1, -1]
        expected = 0
        actual = Solution().pivotIndex(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [-1, 1, 2]
        expected = 2
        actual = Solution().pivotIndex(nums)
        self.assertEqual(expected, actual)
