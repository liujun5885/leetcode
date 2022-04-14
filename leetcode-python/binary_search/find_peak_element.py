# https://leetcode-cn.com/problems/find-peak-element/
import sys
from typing import List
from unittest import TestCase


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-sys.maxsize] + nums + [-sys.maxsize]
        n = len(nums)
        left = 1
        right = n - 2
        while left < right:
            m = (left + right) // 2
            # if it's peak, then return m - 1, because we add -sys.maxsize in front of nums
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m - 1
            elif nums[m - 1] > nums[m]:
                # nums[m - 1] > nums[m], it means, we just need to find from l to m - 1,
                right = m - 1
            elif nums:
                # vice versa
                left = m + 1

        # if it breaks from loop, it means left == right, and all num[left - 1] < num[left] > num[left + 1]
        return left - 1


class TestCases(TestCase):
    def test_1(self):
        nums = [1, 2, 3, 1]
        expected = 2
        actual = Solution().findPeakElement(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        expected = 5
        actual = Solution().findPeakElement(nums)
        self.assertEqual(expected, actual)
