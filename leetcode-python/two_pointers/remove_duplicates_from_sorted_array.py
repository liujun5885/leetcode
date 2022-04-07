# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List
from unittest import TestCase


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] != nums[ans]:
                ans += 1
                nums[ans] = nums[i]

        return ans + 1


class TestCases(TestCase):
    def test_1(self):
        nums = [1, 1, 2]
        expected = 2
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(expected, actual)
