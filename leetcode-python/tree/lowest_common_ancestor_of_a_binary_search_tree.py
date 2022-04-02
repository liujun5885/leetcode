# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root

        while True:
            # if cur.val is smaller than both p and q, it means p, q is in the right
            if ans.val < p.val and ans.val < q.val:
                ans = ans.right
            # if cur.val is bigger than both p and q, it means p, q is in the left
            elif ans.val > p.val and ans.val > q.val:
                ans = ans.left
            # otherwise, it means, cur node is the ancestor of q and p
            else:
                break

        return ans
