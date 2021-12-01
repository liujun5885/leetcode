class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                temp=0
                while (top:= stack.pop()) != '(':
                    temp += top
                if temp:
                    stack.append(temp*2)
                else:
                    stack.append(1)
        return sum(stack)

