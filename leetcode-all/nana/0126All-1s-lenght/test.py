from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        res = []
        for index, value in enumerate(nums):
            if value == 1:
                res.append(index)
        for i in range(len(res)-1):
            if res[i+1]-res[i] <= k:
                return False;
        return True

print(Solution().kLengthApart([1,0,0,1,0,1],2))

