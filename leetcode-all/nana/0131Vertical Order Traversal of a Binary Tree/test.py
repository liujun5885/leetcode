from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, pos, lvl):
            level[pos].append((lvl, root.val))
            if root.left:
                dfs(root.left, pos - 1, lvl + 1)
            if root.right:
                dfs(root.right, pos + 1, lvl + 1)

        level = defaultdict(list)
        dfs(root, 0, 0)
        res = []
        for key, val in sorted(level.items(), key=lambda x: x[0]):
            res.append([v for k, v in sorted(val)])
        return res
