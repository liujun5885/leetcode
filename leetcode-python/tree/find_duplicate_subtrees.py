from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        counter = collections.Counter()
        ans = []

        def preorder(node: TreeNode):
            if not node:
                return "$"

            serial = "{},{},{}".format(node.val, preorder(node.left), preorder(node.right))
            counter[serial] += 1
            if counter[serial] == 2:
                ans.append(node)
            return serial

        preorder(root)

        return ans
