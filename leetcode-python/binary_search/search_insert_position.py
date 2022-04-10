# https://leetcode-cn.com/problems/search-insert-position/

from unittest import TestCase
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s < e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1

        if nums[s] < target:  # if current position is smaller than target, then put target into next position.
            return s + 1
        else:  # otherwise, put it into current position, and put all num from current to next position.
            return s


class TestCases(TestCase):
    def test_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expected = 1
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected = 4
        actual = Solution().searchInsert(nums, target)
        self.assertEqual(expected, actual)
