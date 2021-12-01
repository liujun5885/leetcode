from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        LEN = len(nums)
        l = LEN - 1
        stack = []
        for i in range(LEN):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        stack = []
        r = 0
        for i in range(LEN)[::-1]:
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        return r - l + 1 if r - l + 1 > 0 else 0


if __name__ == '__main__':
    assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert Solution().findUnsortedSubarray([2, 6, 4, 8]) == 2
    assert Solution().findUnsortedSubarray([10, 9, 8, 7, 6, 5]) == 6
    assert Solution().findUnsortedSubarray([1, 2, 3, 4]) == 0
    assert Solution().findUnsortedSubarray([1]) == 0
    assert Solution().findUnsortedSubarray([2, 1]) == 2
