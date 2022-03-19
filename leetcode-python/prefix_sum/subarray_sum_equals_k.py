# https://leetcode-cn.com/problems/subarray-sum-equals-k/

from typing import List
import unittest
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = 0
        pre_sum = defaultdict(int)
        pre_sum[0] = 1

        for i in nums:
            pre += i

            if pre - k in pre_sum:
                ans += pre_sum[pre - k]

            pre_sum[pre] += 1

        return ans


class TestCase(unittest.TestCase):
    def test_01(self):
        nums = [1, 1, 1]
        k = 2
        actual = Solution().subarraySum(nums, k)
        expected = 2
        self.assertEqual(actual, expected)
