class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        rems = len(nums) - k
        for num in nums:
            while res and rems and num<res[-1]:
                res.pop()
                rems -= 1
            res.append(num)
        return res[:k]
        
