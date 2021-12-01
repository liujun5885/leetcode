class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return 0
        left, right = 0, len(nums) - 1               
        while left < right and nums[left] == sorted_nums[left]:
            left = left + 1
        while left < right and nums[right] == sorted_nums[right]:
            right = right - 1
        return right - left + 1
