from typing import List

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d)
        d = sorted(d, key=lambda x:len(x), reverse=True)
        for word in d:
            len_word = len(word)
            lw = 0
            ls = 0
            while ls <= len(s)-1:
                if s[ls] == word[lw]:
                    lw += 1
                ls += 1
                if lw == len_word:
                    return word
        return ""


s = "abpcplea"
d = ["ale","apple","monkey","plea"]
res = Solution().findLongestWord(s, d)
print(res)