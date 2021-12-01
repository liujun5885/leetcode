from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, n in enumerate(nums):
            #if the stack left space < the left ones in num, stack can pop
            while stack and stack[-1] > n and k - len(stack) < len(nums) - i:
                stack.pop()
            if len(stack) < k:
                stack.append(n)
        return stack

nums = [3,4,5,2,6]
k = 2
print(Solution().mostCompetitive(nums, k))
