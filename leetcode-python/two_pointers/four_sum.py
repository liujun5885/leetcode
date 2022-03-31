# https://leetcode-cn.com/problems/4sum/

from typing import List
from unittest import TestCase


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()

        nums = sorted(nums)
        n = len(nums)

        if n < 4:
            return []

        print(nums)

        for i in range(n):
            for j in range(i + 1, n):
                start, end = j + 1, n - 1
                while start < end:
                    while start < end - 1 and nums[start] == nums[start + 1]:
                        start += 1

                    while end > start + 1 and nums[end] == nums[end - 1]:
                        end -= 1
                    if nums[i] + nums[j] + nums[start] + nums[end] == target:
                        ans.add((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                    elif nums[i] + nums[j] + nums[start] + nums[end] > target:
                        end -= 1
                    else:
                        start += 1

        return [*map(lambda x: [*x], ans)]


class TestCases(TestCase):
    def test_1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        actual = Solution().fourSum(nums, target)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_2(self):
        nums = [2, 2, 2, 2, 2]
        target = 8
        expected = [[2, 2, 2, 2]]
        actual = Solution().fourSum(nums, target)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_3(self):
        nums = [2, 2, 2, 2, 2]
        target = 9
        expected = []
        actual = Solution().fourSum(nums, target)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_4(self):
        nums = [-2, -1, -1, 1, 1, 2, 2]
        target = 0
        expected = [[-2, -1, 1, 2], [-1, -1, 1, 1]]
        actual = Solution().fourSum(nums, target)
        self.assertEqual(sorted(expected), sorted(actual))
