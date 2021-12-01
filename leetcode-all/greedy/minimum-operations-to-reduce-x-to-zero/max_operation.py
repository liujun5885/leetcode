from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        if k < nums[0]:
            return 0
        left, count = 0, 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return count


nums1 = [1, 1, 4, 2, 3]
result = Solution().maxOperations(nums1, 5)
assert result == 2
