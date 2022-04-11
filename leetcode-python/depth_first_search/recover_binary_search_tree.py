# https://leetcode-cn.com/problems/recover-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = []
        prev, x, y = None, None, None

        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # if current value is smaller than previous, then it's the wrong one.
            if prev is not None and root.val < prev.val:
                y = root  # the second is the smaller one
                if x is None:  # the first is the bigger one
                    x = prev
                else:
                    break

            prev = root
            root = root.right

        x.val, y.val = y.val, x.val
