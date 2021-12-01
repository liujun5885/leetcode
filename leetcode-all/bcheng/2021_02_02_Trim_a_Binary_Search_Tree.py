# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        while root:
            if root.val<low:
                root = root.right
            elif root.val>high:
                root = root.left
            else:
                break
        pre = root
        cur = root.left
        while cur:
            if cur.val<low:
                pre.left = cur.right
                cur = cur.right
            elif cur.val>=low:
                pre = cur
                cur = cur.left
        pre = root
        cur = root.right
        while cur:
            if cur.val>high:
                pre.right = cur.left
                cur = cur.left
            else:
                pre = cur
                cur = cur.right
        return root