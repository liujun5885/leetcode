from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for it in path.rstrip('/').split('/'):
            if it=='.' or it =="":
                continue
            elif it == "..":
                if len(res)>0:
                    res.pop()
            else:
                res.append(it)
        return '/' + '/'.join(res)

inputs = "/home//foo/"
res = Solution().simplifyPath(inputs)
print(res)
