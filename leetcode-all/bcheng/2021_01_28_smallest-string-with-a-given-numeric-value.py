class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        while n:
            left_min = n - 1
            this = k - left_min
            if this > 26:
                this = 26
            res.append(chr(96 + this))
            k -= this
            n -= 1
        return ''.join(reversed(res))
