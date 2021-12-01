from typing import List


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        tmp = 0
        while dividend >= divisor:
            dividend -= divisor
            tmp += 1
        return sign * tmp


res = Solution().divide(7, 2)
assert res == 3

res = Solution().divide(0, 1)
assert res == 0

res = Solution().divide(-8, 2)
assert res == -4
