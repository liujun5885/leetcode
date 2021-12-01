# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        from itertools import groupby
        root.x=root.y=0
        todo=deque([root])
        visited=[]
        while todo:
            node = todo.popleft()
            visited.append((node.x, node.y, node.val))
            if node.left:
                node.left.x=node.x-1
                node.left.y=node.y+1
                todo.append(node.left)
            if node.right:
                node.right.x=node.x+1
                node.right.y=node.y+1
                todo.append(node.right)
        visited.sort()
        group = groupby(visited, lambda i:i[0])
        return [[i[-1] for i in v] for k,v in group]
