from typing import List


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y>X:
            if Y%2 == 0:
                Y = int(Y/2)
            else:
                Y = Y+1
            res += 1
        return res+X-Y



X = 1024
Y = 1
res = Solution().brokenCalc(X, Y)
print(res)