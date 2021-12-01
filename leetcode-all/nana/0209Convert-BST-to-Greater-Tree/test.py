# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.ct += root.val
            root.val = self.ct
            dfs(root.left)

        self.ct = 0
        dfs(root)
        return root
