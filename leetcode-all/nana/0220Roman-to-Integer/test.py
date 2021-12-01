from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0: return 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        res = 0
        for i in range(len(s) -1):
            if dic[s[i]] < dic[s[i+1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        res += dic[s[-1]]
        return res



s = "MCMXCIV"
res = Solution().romanToInt(s)
print(res)