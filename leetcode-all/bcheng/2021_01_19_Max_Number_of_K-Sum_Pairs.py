from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        for n in counter:
            res += min(counter[n], counter[k-n])
        return res//2
