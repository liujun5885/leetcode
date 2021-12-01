from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for c in S:
            if c.isalpha():
                res = [i + j for i in res for j in [c.upper(), c.lower()]]
            else:
                res = [i + c for i in res]
        return res

S = "a1b2"
res = Solution().letterCasePermutation(S)
print(res)