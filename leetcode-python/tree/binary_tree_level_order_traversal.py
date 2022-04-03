# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        if root is None:
            return ans

        queue = [root]

        while len(queue) > 0:
            cur_q = []
            cur_ans = []
            for i in queue:
                cur_ans.append(i.val)
                if i.left is not None:
                    cur_q.append(i.left)
                if i.right is not None:
                    cur_q.append(i.right)
            ans.append(cur_ans)
            queue = cur_q

        return ans
