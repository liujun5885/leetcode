# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        cur_queue=[]
        next_queue=[root]
        odd=False
        while next_queue:
            # print(next_queue)
            cur_queue = next_queue
            next_queue = []
            last = cur_queue[0]
            if odd and last.val % 2 != 0:
                return False
            if not odd and last.val % 2 ==0:
                return False
            if last.left:
                next_queue.append(last.left)
            if last.right:
                next_queue.append(last.right)
            for node in cur_queue[1:]:
                if odd:
                    if node.val % 2 !=0 or node.val>= last.val:
                        # print((odd,node.val,last.val))
                        return False
                if not odd:
                    if node.val %2 ==0 or node.val<=last.val:
                        # print((odd,node.val,last.val))
                        return False
                last = node
                if last.left:
                    next_queue.append(last.left)
                if last.right:
                    next_queue.append(last.right)
            odd = not odd
        return True
