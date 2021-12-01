from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False


s = "anagram"
t = "nagaram"
res = Solution().isAnagram(s, t)
print(res)