class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, n in enumerate(nums):
            if n:
                if last and i-last<=k:
                    return False
                last = i
        return True
