# https://leetcode-cn.com/problems/3sum-closest/
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = 10000000

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                first += 1

            second = first + 1
            third = n - 1
            while second < third:
                sum3 = nums[first] + nums[second] + nums[third]
                if sum3 == target:
                    return sum3

                if abs(target - sum3) < abs(target - ans):
                    ans = sum3

                if sum3 > target:
                    third -= 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                else:
                    second += 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1

        return ans


class TestSolution:
    def test_case01(self):
        nums = [-1, 2, 1, -4]
        target = 1
        actual = Solution().threeSumClosest(nums, target)
        expected = 2
        assert actual == expected

    def test_case02(self):
        nums = [0, 0, 0]
        target = 1
        actual = Solution().threeSumClosest(nums, target)
        expected = 0
        assert actual == expected
