from collections import Counter
from typing import List


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1, c2 = Counter(word1), Counter(word2)
        return (sorted(c1.values()) == sorted(c2.values())) and (c1.keys() == c2.keys())


w1='abbccc'
w2='cccbba'
result = Solution().closeStrings(w1, w2)
print(result)
