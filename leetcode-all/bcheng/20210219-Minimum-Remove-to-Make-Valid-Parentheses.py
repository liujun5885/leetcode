class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = []
        opened = 0
        for i in s:
            if i == '(':
                opened += 1
            elif i == ')':
                if opened:
                    opened -= 1
                else:
                    continue
            temp.append(i)
        res = []
        opened = 0
        for i in reversed(temp):
            if i == ')':
                opened += 1
            elif i == '(':
                if opened:
                    opened -= 1
                else:
                    continue
            res.append(i)
        return ''.join(reversed(res))
