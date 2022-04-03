# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/

from typing import Optional
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -sys.maxsize

        # max_path = max(max_path, node.val + value of left + value of righ)
        def get_max_path_of_node(node: TreeNode):
            nonlocal ans
            if node is None:
                return 0

            left = max(get_max_path_of_node(node.left), 0)
            right = max(get_max_path_of_node(node.right), 0)

            ans = max(ans, node.val + left + right)

            return node.val + max(left, right)

        get_max_path_of_node(root)

        return ans
