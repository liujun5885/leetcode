from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        q = [root]
        while q:
            tmp = []
            s = 0
            for n in q:
                s += n.val
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            res.append(s / len(q))
            q = tmp
        return res