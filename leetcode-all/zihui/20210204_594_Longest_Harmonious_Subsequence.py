class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m = 0
        c = Counter(nums)
        
        for k in c.keys():
            k_1 = k + 1
            if not c.get(k_1):
                continue
            m = max(c.get(k_1, 0) + c.get(k), m)
        return m















