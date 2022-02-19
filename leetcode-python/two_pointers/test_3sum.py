# https://leetcode-cn.com/problems/3sum/submissions/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        ans = []
        nums = sorted(nums)
        n = len(nums)

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                first += 1
                continue

            third = n - 1
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                    continue

                left = target - nums[first] - nums[second]
                while second < third and nums[third] > left:
                    third -= 1

                if second == third:
                    break

                if left == nums[third]:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


class TestSolution:
    def test_case01(self):
        nums = [-1, 0, 1, 2, -1, -4]
        actual = Solution().threeSum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted(actual) == sorted(expected)

    def test_case02(self):
        nums = []
        actual = Solution().threeSum(nums)
        expected = []
        assert sorted(actual) == sorted(expected)

    def test_case03(self):
        nums = [0]
        actual = Solution().threeSum(nums)
        expected = []
        assert sorted(actual) == sorted(expected)

    def test_case04(self):
        nums = [0, 0, 0, 1, -1]
        actual = Solution().threeSum(nums)
        expected = [[0, 0, 0], [-1, 0, 1]]
        assert sorted(actual) == sorted(expected)
