# https://leetcode-cn.com/problems/increasing-triplet-subsequence/

from typing import List
import sys
from unittest import TestCase


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        first = nums[0]
        second = sys.maxsize

        for i in range(n):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]

        return False


class TestCases(TestCase):
    def test_1(self):
        nums = [1, 2, 3, 4, 5]
        expected = True
        actual = Solution().increasingTriplet(nums)
        self.assertEqual(actual, expected)
