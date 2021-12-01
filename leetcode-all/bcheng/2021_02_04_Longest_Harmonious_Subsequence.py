class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        res = 0
        for k in c:
            count = c[k]+c[k+1] if c[k+1] else 0
            if count>res:
                res = count
        return res
