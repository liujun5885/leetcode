from typing import List


class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num >0:
            num = num -1 if num & 1 else num >>1
            count += 1
        return count
num=14
res = Solution().numberOfSteps(num)
print(res)