from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        new_arr = sorted(nums)
        if new_arr == nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != new_arr[i]:
                start = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != new_arr[j]:
                end = j
                break

        return end - start + 1


nums = [1, 2, 4, 3, 5, 7, 6]
res = Solution().findUnsortedSubarray(nums)
print(res)
