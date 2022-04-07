# https://leetcode-cn.com/problems/single-number/

from typing import List
from functools import reduce
from unittest import TestCase


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        a ^ a = 0
        0 ^ a = a
        a ^ b = b ^ a
        because every element appears twice except for one, so we XOR all of them,
        it's equal to the element which appears onece.
        """
        return reduce(lambda x, y: x ^ y, nums)


class TestCases(TestCase):
    def test_1(self):
        nums = [2, 2, 1]
        expected = 1
        actual = Solution().singleNumber(nums)
        self.assertEqual(expected, actual)
