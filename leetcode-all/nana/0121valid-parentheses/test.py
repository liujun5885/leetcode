from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        dict1 = {')': '(', ']': '[', '}': '{'}
        for elem in s:
            if elem in dict1.values():
                res.append(elem)
            elif res and dict1.get(elem) == res[-1]:
                res.pop()
            else:
                return False

        return not res


s = '['
res = Solution().isValid(s)
print(res)
