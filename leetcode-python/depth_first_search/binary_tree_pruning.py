# https://leetcode-cn.com/problems/binary-tree-pruning/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return True

            remove_left = dfs(node.left)
            remove_right = dfs(node.right)
            if remove_left:
                node.left = None
            if remove_right:
                node.right = None

            return remove_left and remove_right and node.val != 1

        if dfs(root) and root.val != 1:  # check if we also need to remove root
            return None

        return root
