class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for idx, val in enumerate(s):
            if val == '(':
                stack.append(idx)
            elif val == ')':
                if stack:
                    stack.pop()
                else:
                    s[idx] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)

