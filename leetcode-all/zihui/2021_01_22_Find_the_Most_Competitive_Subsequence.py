class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        stack = [nums[0]]
        for i in range(1, len(nums)):
            while stack and stack[-1] > nums[i] and k - len(stack) < len(nums) - i:
                stack.pop()
            stack.append(nums[i])
        return stack[:k]
