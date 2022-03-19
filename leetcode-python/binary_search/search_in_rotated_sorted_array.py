# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        if n == 1:
            return 0 if nums[0] == target else -1

        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if nums[0] <= nums[mid]:  # 0 to mid, the num is sequential
                if nums[mid] < target or target < nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


class TestCases(unittest.TestCase):
    def test_case_01(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        actual = Solution().search(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def test_case_02(self):
        nums = [3, 1]
        target = 1
        actual = Solution().search(nums, target)
        expected = 1
        self.assertEqual(actual, expected)
