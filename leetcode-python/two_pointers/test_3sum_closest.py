# https://leetcode-cn.com/problems/3sum-closest/
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return 0


class TestSolution:
    def test_case(self):
        nums = [-1, 2, 1, -4]
        target = 1
        actual = Solution().threeSumClosest(nums, target)
        expected = 2
        assert actual == expected
