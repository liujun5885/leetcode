class Solution:
    def isValid(self, s: str) -> bool:
        l_r_mappings = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for i in s:
            if i in l_r_mappings.values():
                stack.append(i)
            else: 
                if not stack:
                    return False
                if stack.pop() != l_r_mappings.get(i):
                    return False
        if stack:
            return False
        return True

