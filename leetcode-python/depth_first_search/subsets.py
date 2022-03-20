# https://leetcode-cn.com/problems/subsets/

from typing import List
from copy import copy
import unittest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        target = []

        def dfs(i: int):
            if i == len(nums):
                ans.append(copy(target))
                return

            target.append(nums[i])
            dfs(i + 1)
            target.pop()
            dfs(i + 1)

        dfs(0)

        return ans


class TestCases(unittest.TestCase):
    def test_01(self):
        nums = [1, 2, 3]
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        actual = Solution().subsets(nums)
        self.assertListEqual(sorted(actual), sorted(expected))
