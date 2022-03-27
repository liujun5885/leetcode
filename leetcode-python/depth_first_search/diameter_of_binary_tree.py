# https://leetcode-cn.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.

from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if node is None:
                return 0

            left_nodes = dfs(node.left)
            right_nodes = dfs(node.right)

            # the path = left_nodes + right_nodes + node(1) - 1 = left_nodes + right_nodes
            ans = max(ans, left_nodes + right_nodes)

            # return max of the number of nodes
            return max(left_nodes, right_nodes) + 1

        dfs(root)

        return ans
