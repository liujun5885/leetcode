import functools

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex = []
        i = 0
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == '*':
                regex.append(p[i: i + 2])
                i += 2
            else:
                regex.append(p[i])
                i += 1

        @functools.cache
        def match(x, y):
            if x == len(s) and y == len(regex):
                return True
            if x == len(s):
                return all([i[-1]=='*' for i in regex[y:]])
            if y == len(regex):
                return False
            if len(regex[y]) == 1:
                if s[x] != regex[y] and regex[y] != '.':
                    return False
                return match(x + 1, y + 1)
            if s[x] == regex[y][0] or regex[y][0] == '.':
                return match(x, y + 1) or match(x + 1, y)
            return match(x, y + 1)

        return match(0, 0)
