from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [x for x in range(1, len(nums) + 1)]
        end = []
        for i in nums:
            if i in result:
                result.remove(i)
            else:
                end.append(i)
        return end + result
