from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        compared = [x for x in range(0, len(nums) + 1)]
        for value in compared:
            if value not in nums:
                return value
