# https://leetcode-cn.com/problems/number-of-valid-subarrays/

from typing import List
from unittest import TestCase


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        return ans


class TestCases(TestCase):
    def test_1(self):
        nums = [1, 4, 2, 5, 3]
        expected = 11
        actual = Solution().validSubarrays(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [3, 2, 1]
        expected = 3
        actual = Solution().validSubarrays(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [2, 2, 2]
        expected = 6
        actual = Solution().validSubarrays(nums)
        self.assertEqual(expected, actual)
