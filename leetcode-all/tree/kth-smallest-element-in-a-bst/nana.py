from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        # Compare the new value with the parent node
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        self.inorder(root, res)
        return res[k - 1]

    def inorder(self, root, res):
        if root is None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


root = TreeNode(5)
root.insert(3)
root.insert(6)
root.insert(2)
root.insert(4)
root.insert(1)
root.PrintTree()
value = Solution().kthSmallest(root, 3)
print(value)
