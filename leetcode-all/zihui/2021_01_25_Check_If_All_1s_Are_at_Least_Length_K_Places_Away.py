class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = None
        for idx, n in enumerate(nums):
            if n == 1:
                if prev is not None and idx > 0 and idx - prev - 1 < k:
                    return False
                prev = idx
        return True
