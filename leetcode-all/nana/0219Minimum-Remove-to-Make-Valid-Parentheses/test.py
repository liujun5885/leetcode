from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        s = list(s)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                if char == ")":
                    if stack:
                        stack.pop()
                    else:
                        s[i] = ""
        while stack:
            s[stack.pop()] = ""
        return "".join(s)


s = "a)b(c)d"
res = Solution().minRemoveToMakeValid(s)
print(res)