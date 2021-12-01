class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """sliding window: find the longest subarry that sums up to sum(nums) - x"""
        
        if sum(nums) < x:
            return -1
        
        if sum(nums) == x:
            return len(nums)
        
        target = sum(nums) - x
        l = r = 0
        max_len = 0
        curr_sum = 0
        
        while r < len(nums):
            if curr_sum + nums[r] <= target:
                curr_sum += nums[r]
                r += 1
                if curr_sum == target:
                    max_len = max(max_len, r - l)
            elif l == r:
                l += 1
                r += 1
            else:
                curr_sum -= nums[l]
                l += 1
        
        return len(nums) - max_len if max_len != 0 else -1
