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

            if prev is not None and root.val < prev.val:
                y = root
                if x is None:
                    x = prev
                else:
                    break

            prev = root
            root = root.right

        x.val, y.val = y.val, x.val
