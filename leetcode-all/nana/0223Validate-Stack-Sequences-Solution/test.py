from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        #print(stack)
        return not stack


pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
res = Solution().validateStackSequences(pushed, popped)
print(res)


pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 2, 1]
res = Solution().validateStackSequences(pushed, popped)
print(res)