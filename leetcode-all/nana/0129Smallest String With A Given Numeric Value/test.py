from typing import List


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n
        while n > 0 and k > 0:
            if k > 25:
                res[n - 1] = 'z'
                k = k - 25
            else:
                res[n - 1] = chr(ord('a') + k)
                k = 0
            n = n - 1
        return ''.join(res)


n = 3
k = 25
print(Solution().getSmallestString(n, k))
