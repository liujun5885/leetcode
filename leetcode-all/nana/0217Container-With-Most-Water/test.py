from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            res = max(res, min(height[r],height[l])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


height = [4,3,2,1,4]
res = Solution().maxArea(height)
print(res)