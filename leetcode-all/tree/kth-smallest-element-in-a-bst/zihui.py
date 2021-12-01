# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ret = None

        def traverse(node: TreeNode):
            nonlocal k, ret
            if node.left:
                traverse(node.left)
            k -= 1
            if k == 0:
                ret = node.val
                return
            if node.right:
                traverse(node.right)
        traverse(root)
        return ret
