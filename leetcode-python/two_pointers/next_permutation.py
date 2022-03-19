# https://leetcode-cn.com/problems/next-permutation/

import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i > -1:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        l = i + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


class TestCases(unittest.TestCase):
    def test_01(self):
        nums = [1, 2, 3]
        Solution().nextPermutation(nums)
        expected = [1, 3, 2]
        self.assertEqual(nums, expected)

    def test_02(self):
        nums = [3, 2, 1]
        Solution().nextPermutation(nums)
        expected = [1, 2, 3]
        self.assertEqual(nums, expected)

    def test_03(self):
        nums = [1, 1, 5]
        Solution().nextPermutation(nums)
        expected = [1, 5, 1]
        self.assertEqual(nums, expected)

    def test_04(self):
        nums = [1, 3, 2]
        Solution().nextPermutation(nums)
        expected = [2, 1, 3]
        self.assertEqual(nums, expected)

    def test_05(self):
        nums = [2, 3, 1]
        Solution().nextPermutation(nums)
        expected = [3, 1, 2]
        self.assertEqual(nums, expected)
