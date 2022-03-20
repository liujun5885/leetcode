# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List
from unittest import TestCase


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                start = mid
                end = mid
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1

                return [start + 1, end - 1]
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return ans


class TestCases(TestCase):
    def test_case_01(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        actual = Solution().searchRange(nums, target)
        self.assertEqual(actual, expected)

    def test_case_02(self):
        nums = []
        target = 8
        expected = [-1, -1]
        actual = Solution().searchRange(nums, target)
        self.assertEqual(actual, expected)

    def test_case_03(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        actual = Solution().searchRange(nums, target)
        self.assertEqual(actual, expected)
